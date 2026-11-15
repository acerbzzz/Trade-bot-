"""Independent paper replays, one strategy per worker minute."""
import pandas as pd

from engine import advance
from risk_manager import new_account

NAMES = ("trend", "reversion", "breakout", "momentum")
BAR = pd.Timedelta(minutes=15)


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
    cursor = pd.Timestamp(account["cursor"] or state["start"])
    if latest < cursor:
        raise ValueError("Scorecard feed moved backward")
    times = pd.date_range(cursor, latest, freq=BAR)
    views = {}
    for symbol, frame in frames.items():
        if not times.isin(frame.index).all() or frame.index.get_loc(cursor) < config["history"]:
            raise ValueError("Insufficient continuous history for scorecard")
        views[symbol] = frame.assign(enter=frame[name + "_enter"], exit=frame[name + "_exit"])
    for t in times[1:]:
        _, closed = advance(config, account, views, t)
        card["closed"] += len(closed)
        # All finalists get the same fresh portfolio and validation dates.
        if "validation_start" in state and t > pd.Timestamp(state["validation_start"]) and name in state["finalists"]:
            validation = card.setdefault("validation", new_account(config))
            _, exits = advance(config, validation, views, t)
            card["validation_closed"] = card.get("validation_closed", 0) + len(exits)
            if t == pd.Timestamp(state["validation_start"]) + 96 * BAR:
                pnl = validation["equity"] - config["equity"]
                card["validation_pnl"] = pnl
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
    results = state.get("last_result", {})
    if results:
        best = max(results.values())
        leaders = [n for n in results if results[n] == best]
        rows.append("\nValidation leader: " + (", ".join(leaders) if best > 0 else "None profitable"))
    return rows
