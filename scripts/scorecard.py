"""Independent paper replays, one strategy per worker minute."""
import pandas as pd

from engine import advance
from risk_manager import new_account

DESK_NAMES = ("trend", "reversion", "breakout", "momentum")
NAMES = DESK_NAMES + ("relative_strength", "vwap_pullback", "failed_breakdown")
BAR = pd.Timedelta(minutes=15)


def trial_step(name, config, account, frames, t):
    if name != "failed_breakdown":
        return advance(config, account, frames, t)
    prior = t - BAR
    for symbol, frame in frames.items():
        position = account["positions"].get(symbol)
        frame.at[prior, "exit"] = bool(position and frame.at[prior, "close"] < position["reclaimed_low"])
    opened, closed = advance(config, account, frames, t)
    for entry in opened:
        symbol = entry["symbol"]
        if symbol in account["positions"]:
            account["positions"][symbol]["reclaimed_low"] = float(frames[symbol].at[prior, "failed_breakdown_level"])
    return opened, closed


def benchmark_value(initial, cost, start_prices, end_prices):
    # Equal cash allocation, model entry and liquidation with the trial fee/slippage.
    entry_factor, exit_factor = cost
    return sum(initial / len(start_prices) / (price * entry_factor)
               * end_prices[symbol] * exit_factor for symbol, price in start_prices.items())


def tick(state, config, frames, latest, now):
    minute = str(now.floor("min"))
    if state.get("minute") == minute:
        return
    # Every strategy starts with the same 24 hours of closed historical bars.
    state.setdefault("start", str(latest - 96 * BAR))
    cards = state.setdefault("cards", {})
    name = NAMES[state.get("turn", 0)]
    card = cards.setdefault(name, {"account": new_account(config), "closed": 0})
    account = card["account"]
    if not account["cursor"] and name not in DESK_NAMES:
        earliest = max(d.index[config["history"]] for d in frames.values())
        card.setdefault("start", str(max(pd.Timestamp(state["start"]), earliest)))
    cursor = pd.Timestamp(account["cursor"] or card.get("start", state["start"]))
    if latest < cursor:
        raise ValueError("Scorecard feed moved backward")
    times = pd.date_range(cursor, latest, freq=BAR)
    views = {}
    for symbol, frame in frames.items():
        if not times.isin(frame.index).all() or frame.index.get_loc(cursor) < config["history"]:
            raise ValueError("Insufficient continuous history for scorecard")
        views[symbol] = frame.assign(enter=frame[name + "_enter"], exit=frame[name + "_exit"])
    for t in times[1:]:
        _, closed = trial_step(name, config, account, views, t)
        card["closed"] += len(closed)
        # All finalists get the same fresh portfolio and validation dates.
        if "validation_start" in state and t > pd.Timestamp(state["validation_start"]) and name in state["finalists"]:
            validation = card.setdefault("validation", new_account(config))
            _, exits = trial_step(name, config, validation, views, t)
            card["validation_closed"] = card.get("validation_closed", 0) + len(exits)
            if t == pd.Timestamp(state["validation_start"]) + 96 * BAR:
                pnl = validation["equity"] - config["equity"]
                card["validation_pnl"] = pnl
    if name == "relative_strength" and len(times) > 1:
        prices = card.setdefault("benchmark_entry", {s: float(d.at[times[1], "open"]) for s, d in frames.items()})
        fee, slip = config["fee_bps"] / 10000, config["slip_bps"] / 10000
        costs = ((1 + slip) * (1 + fee), (1 - slip) * (1 - fee))
        ends = {s: d.at[latest, "close"] for s, d in frames.items()}
        card["benchmark_equity"] = float(benchmark_value(config["equity"], costs, prices, ends))
    if (card["closed"] and account["balance"] > config["equity"]
            and account["equity"] > config["equity"]):
        card.setdefault("qualified", str(latest))
    state.update(turn=(NAMES.index(name) + 1) % len(NAMES), minute=minute)
    if state["turn"] == 0:
        previous = state.get("finalists", [])
        if previous and not all("validation_pnl" in cards[n] for n in previous):
            return
        if previous:
            state["last_result"] = {n: cards[n]["validation_pnl"] for n in previous}
            for n in previous:
                for key in ("validation", "validation_closed", "validation_pnl"):
                    cards[n].pop(key, None)
        qualified = [n for n in NAMES if cards[n].get("qualified")]
        if len(qualified) >= 2:
            state.update(finalists=qualified, validation_start=str(latest))


def report(state, initial):
    rows = ["", "## Strategy trials", "",
            "One independent paper trial per worker minute. Net P&L includes modeled costs.",
            "", "| Strategy | Closed | Realized P&L | Shortlisted | Next-day validation P&L |",
            "|---|---:|---:|---|---:|"]
    for name in NAMES:
        card = state["cards"].get(name)
        if not card:
            rows.append(f"| {name} | — | — | Awaiting first test | — |")
            continue
        pnl = card["account"]["balance"] - initial
        later = state.get("last_result", {}).get(name)
        rows.append(f"| {name} | {card['closed']} | ${pnl:+.2f} | "
                    + ("Yes" if card.get("qualified") else "Pending") + " | "
                    + ("—" if later is None else f"${later:+.2f}") + " |")
    relative = state["cards"].get("relative_strength", {})
    if "benchmark_equity" in relative:
        rows.append(f"\nRelative strength trial equity: ${relative['account']['equity']:.2f}. "
                    f"50/50 BTC–ETH buy-and-hold liquidation value: ${relative['benchmark_equity']:.2f}.")
    results = state.get("last_result", {})
    if results:
        best = max(results.values())
        leaders = [n for n in results if results[n] == best]
        rows.append("\nValidation leader: " + (", ".join(leaders) if best > 0 else "None profitable"))
    return rows
