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
    d = normalize(d)
    if not STEP <= now - d.index[-1] < 2*STEP:
        raise RuntimeError("Feed stale or ahead of clock")
    return prepare(d, CONFIG)


def main():
    now = pd.Timestamp.now(tz="UTC")
    frames = {s: market_frame(s, now) for s in CONFIG["symbols"]}
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
    # Act only on a signal previously observed and saved by this runner.
    # Other elapsed bars can close existing positions but cannot open new ones.
    for t in times[1:]:
        eligible = t == cursor + STEP
        if eligible:
            for s, d in frames.items():
                d.at[cursor,"enter"] = a["signals"][s]
        opened, closed = advance(CONFIG, a, frames, t, allow_entries=eligible)
        for kind, records in (("open",opened),("close",closed)):
            events.extend(dict(kind=kind,time=str(t),**r) for r in records)
    if a["cursor"] is None or latest > cursor:
        a["signals"] = {s:bool(d.at[latest,"enter"]) for s,d in frames.items()}
    a["cursor"] = str(latest)
    a["closed"] = a.get("closed",0) + sum(e["kind"]=="close" for e in events)
    path.write_text(json.dumps(a,indent=2,allow_nan=False)+"\n")
    with (ROOT / "events.jsonl").open("a") as f:
        for event in events:
            f.write(json.dumps(event,allow_nan=False)+"\n")
    status = "Drawdown halt" if a["halted"] else "Daily loss halt" if a["day_halt"] else "Monitoring"
    lines = ["# Crypto paper desk", "", f"**{status}** · Kraken spot · 15-minute candles",
             "", f"Latest completed candle ended **{latest+STEP:%Y-%m-%d %H:%M} UTC**.",
             "", "| Paper equity | Open positions | Closed trades |",
             "|---:|---:|---:|", f"| ${a['equity']:,.2f} | {len(a['positions'])} | {a['closed']} |",
             "", "| Market | Last close | Trend strategy |", "|---|---:|---|"]
    for s,d in frames.items():
        signal = "In position" if s in a["positions"] else "Entry signal" if a["signals"][s] else "Waiting for signal"
        lines.append(f"| {s} | ${d.at[latest,'close']:,.2f} | {signal} |")
    lines += ["", "Started with $200 simulated USD. Entries and exits are modeled from candles. No broker orders.",
              "", "[Refresh history](https://github.com/acerbzzz/Trade-bot-/actions/workflows/forward-paper.yml)"]
    (ROOT/"README.md").write_text("\n".join(lines)+"\n")


if __name__ == "__main__":
    main()
