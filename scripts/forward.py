"""Advance a simulated portfolio using only public Kraken candles."""
import json
import sys
from pathlib import Path
from urllib.request import urlopen

import pandas as pd

from config import load
from engine import advance
from exchange import normalize
from risk_manager import new_account
from strategies import prepare

from scorecard import DESK_NAMES as STRATEGIES, report, tick
from trial_signals import add_signals

ROOT = Path(sys.argv[1])
CONFIG = load(sys.argv[2])
CONFIG.update(venue="kraken", symbols={"BTC/USD": 0.00001, "ETH/USD": 0.0001})
STEP = pd.Timedelta(minutes=15)


def market_frame(symbol, now):
    pair = {"BTC/USD": "XBTUSD", "ETH/USD": "ETHUSD"}[symbol]
    with urlopen(f"https://api.kraken.com/0/public/OHLC?pair={pair}&interval=15", timeout=20) as response:
        data = json.load(response)
    if data["error"]:
        raise RuntimeError(str(data["error"]))
    rows, = (v for k, v in data["result"].items() if k != "last")
    # Kraken's trailing record is provisional.
    d = pd.DataFrame(rows[:-1], columns="timestamp open high low close vwap volume count".split())
    d["timestamp"] = pd.to_datetime(d.timestamp, unit="s", utc=True)
    bar_vwap = pd.Series(d.vwap.astype(float).to_numpy(), index=d.timestamp)
    d = normalize(d)
    d["bar_vwap"] = bar_vwap.reindex(d.index)
    if not STEP <= now - d.index[-1] < 2*STEP:
        raise RuntimeError("Feed stale or ahead of clock")
    return strategy_frame(d)


def strategy_frame(d):
    base = None
    for name in STRATEGIES:
        signals = prepare(d, dict(CONFIG, strategy=name))
        if base is None:
            base = signals.copy()
        for side in ("enter", "exit"):
            base[f"{name}_{side}"] = signals[side]
    return base


def candidates(frames, t):
    return {symbol: [name for name in STRATEGIES if frame.at[t, f"{name}_enter"]]
            for symbol, frame in frames.items()}


def step_portfolio(account, frames, previous, t, saved):
    owners = {s: p["strategy"] for s, p in account["positions"].items()}
    for symbol, frame in frames.items():
        signals = saved.get(symbol, [])
        frame.at[previous, "enter"] = bool(signals)
        if signals and symbol not in owners:
            owners[symbol] = signals[0]
        owner = owners.get(symbol)
        frame.at[previous, "exit"] = bool(owner and frame.at[previous, f"{owner}_exit"])

    opened, closed = advance(CONFIG, account, frames, t, allow_entries=bool(saved))
    for record in opened + closed:
        record["strategy"] = owners[record["symbol"]]
    for symbol, position in account["positions"].items():
        position["strategy"] = owners[symbol]
    return opened, closed


def main():
    now = pd.Timestamp.now(tz="UTC")
    frames = {s: market_frame(s, now) for s in CONFIG["symbols"]}
    add_signals(frames)
    latest, = {d.index[-1] for d in frames.values()}
    path = ROOT / "account.json"
    a = json.loads(path.read_text()) if path.exists() else new_account(CONFIG)
    if a.get("settings", CONFIG) != CONFIG:
        raise RuntimeError("Existing portfolio settings differ")
    a["settings"] = CONFIG
    cursor = pd.Timestamp(a["cursor"]) if a["cursor"] else latest
    if latest < cursor:
        raise RuntimeError("Market feed moved backward")
    times = pd.date_range(cursor, latest, freq=STEP)
    for d in frames.values():
        if not times.isin(d.index).all():
            raise RuntimeError("Missing candles. Preserve account and restore history.")
    events = []
    for position in a["positions"].values():
        position.setdefault("strategy", "trend")
    saved = a.get("strategy_signals")
    if saved is None:
        # Before migration only trend signals had actually been observed.
        saved = {s: ["trend"] if v else [] for s, v in a.get("signals", {}).items()}
    for t in times[1:]:
        opened, closed = step_portfolio(a, frames, t - STEP, t, saved)
        saved = {}  # Missed polling intervals may close a position but cannot open one.
        for kind, records in (("open", opened), ("close", closed)):
            events.extend(dict(kind=kind, time=str(t), **r) for r in records)
    if a["cursor"] is None or latest > cursor or "strategy_signals" not in a:
        a["strategy_signals"] = candidates(frames, latest)
    a["signals"] = {s: "trend" in names for s, names in a["strategy_signals"].items()}
    a["cursor"] = str(latest)
    a["closed"] = a.get("closed",0) + sum(e["kind"]=="close" for e in events)
    trials = a.setdefault("strategy_trials", {})
    tick(trials, CONFIG, frames, latest, now)
    path.write_text(json.dumps(a,indent=2,allow_nan=False)+"\n")
    with (ROOT / "events.jsonl").open("a") as f:
        for event in events:
            f.write(json.dumps(event,allow_nan=False)+"\n")
    status = "Drawdown halt" if a["halted"] else "Daily loss halt" if a["day_halt"] else "Monitoring"
    lines = ["# Crypto paper desk", "", f"**{status}** · Kraken spot · 15-minute candles",
             "", f"Latest completed candle ended **{latest+STEP:%Y-%m-%d %H:%M} UTC**.",
             "", "| Paper equity | Open positions | Closed trades |",
             "|---:|---:|---:|", f"| ${a['equity']:,.2f} | {len(a['positions'])} | {a['closed']} |",
             "", "| Market | Last close | Trend | Mean reversion | Breakout | Momentum |",
             "|---|---:|---|---|---|---|"]
    for symbol, frame in frames.items():
        position = a["positions"].get(symbol, {})
        statuses = []
        for name in STRATEGIES:
            if position.get("strategy") == name:
                status = "In position"
            elif name in a["strategy_signals"][symbol]:
                status = "Entry signal"
            else:
                status = "Waiting"
            statuses.append(status)
        lines.append(f"| {symbol} | ${frame.at[latest,'close']:,.2f} | " + " | ".join(statuses) + " |")
    lines += report(trials, CONFIG["equity"])
    lines += ["", "Started with $200 simulated USD. Entries and exits are modeled from candles. No broker orders.",
              "", "[Refresh history](https://github.com/acerbzzz/Trade-bot-/actions/workflows/forward-paper.yml)"]
    (ROOT/"README.md").write_text("\n".join(lines)+"\n")


if __name__ == "__main__":
    main()
