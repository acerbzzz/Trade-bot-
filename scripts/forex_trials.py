"""Read-only EUR/USD rolling holdout research. No broker client or account credentials."""
import json
import sys
from pathlib import Path
from urllib.request import Request, urlopen

import numpy as np
import pandas as pd
from ta.trend import PSARIndicator
from ta.volatility import AverageTrueRange

# Five-decimal EUR/USD quotation. Model a 1-pip spread plus 0.1 pip slippage per side.
POINT = 0.00001
SIDE_COST = 6 * POINT
SETUPS = (("Bali scalper", "1h", "3mo"), ("Weekly candle reversal", "1wk", "5y"),
          ("Parabolic EMA", "15m", "1mo"))


def fetch(interval, span, now):
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/EURUSD=X?range={span}&interval={interval}"
    with urlopen(Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=15) as response:
        result = json.load(response)["chart"]["result"][0]
    index = pd.to_datetime(result["timestamp"], unit="s", utc=True)
    bars = pd.DataFrame(result["indicators"]["quote"][0], index=index)
    bars = bars[["open", "high", "low", "close"]].dropna().sort_index()
    if interval == "1wk":
        local = bars.index.tz_convert(result["meta"]["exchangeTimezoneName"])
        ends = (local.normalize() + pd.DateOffset(weeks=1)).tz_convert("UTC")
        bars = bars[(local.weekday == 0) & (local.hour == 0) & (local.minute == 0) & (ends <= now)]
    else:
        step = pd.Timedelta("15min" if interval == "15m" else "1h")
        bars = bars[(bars.index == bars.index.floor(step)) & (bars.index + step <= now)]
    if (len(bars) < 180 or bars.index.has_duplicates or not np.isfinite(bars).all().all()
            or (bars <= 0).any().any() or (bars.high < bars.low).any()):
        raise ValueError("Insufficient or invalid completed OHLC data")
    # Some weekly vendor ranges omit the opening quote. Include observed endpoints.
    bars["low"] = bars[["low", "open", "close"]].min(axis=1)
    bars["high"] = bars[["high", "open", "close"]].max(axis=1)
    return bars


def stochastic(value, low, high):
    floor = low.rolling(32).min()
    spread = high.rolling(32).max() - floor
    return ((value - floor) * 100 / spread.where(spread != 0)).where(spread != 0, 0)


def scalper(d):
    # Indicator calculations follow the Bali template's MT4 sources. DSS defaults
    # are momentum 14, stochastic 32, smoothing 9 and signal 5.
    center = (2 * d.close + d.close.shift()) / 3
    upper, lower = center * 1.002, center * 0.998
    direction = np.zeros(len(d), dtype=int)
    for i in range(2, len(d)):
        direction[i] = direction[i - 1]
        if d.close.iat[i] > upper.iat[i - 1]:
            direction[i] = 1
        elif d.close.iat[i] < lower.iat[i - 1]:
            direction[i] = -1
        if direction[i] > 0:
            lower.iat[i] = max(lower.iat[i], lower.iat[i - 1])
        else:
            upper.iat[i] = min(upper.iat[i], upper.iat[i - 1])
    trend = pd.Series(direction, index=d.index)
    mom = d.diff(14)
    first = stochastic(mom.close, mom.low, mom.high).ewm(span=9, adjust=False).mean()
    dss = stochastic(first, first, first).ewm(span=9, adjust=False).mean()
    signal = dss.ewm(span=5, adjust=False).mean()
    color = np.sign(dss.diff()).replace(0, np.nan).ffill()
    weights = np.arange(1, 49)
    lwma = d.close.rolling(48).apply(lambda x: np.dot(x, weights) / weights.sum(), raw=True)
    return ((trend.diff() == 2) & (d.close > lwma) & (color > 0) & (dss > signal),
            (trend.diff() == -2) & (d.close < lwma) & (color < 0) & (dss < signal))


def signals(name, d):
    if name == "Bali scalper":
        return scalper(d)
    if name == "Weekly candle reversal":
        body = d.close - d.open
        large = body.abs() > body.abs().shift().rolling(20).quantile(.75)
        return large & (body < 0), large & (body > 0)
    fast, medium, slow = [d.close.ewm(span=n, adjust=False).mean() for n in (5, 25, 50)]
    sar = PSARIndicator(d.high, d.low, d.close).psar()
    above, below = (fast > medium) & (fast > slow), (fast < medium) & (fast < slow)
    return above & ~above.shift(fill_value=False) & (sar < d.low), below & ~below.shift(fill_value=False) & (sar > d.high)


def replay(name, d):
    longs, shorts = signals(name, d)
    direction = longs.astype(int) - shorts.astype(int)
    atr = AverageTrueRange(d.high, d.low, d.close).average_true_range()
    cash = peak = equity = day_start = 200.0
    day = position = None
    halted = daily_halt = False
    trades = []
    start = max(150, int(.7 * len(d)))
    for i in range(start, len(d)):
        t, bar = d.index[i], d.iloc[i]
        if day != t.date():
            day, day_start, daily_halt = t.date(), equity, False
        side = direction.iat[i - 1]
        if position is None and side and not (halted or daily_halt):
            weekly = name == "Weekly candle reversal"
            distance = 120 * POINT if weekly else 2 * atr.iat[i - 1]
            loss = distance + 2 * SIDE_COST
            reward = 60 * POINT if weekly else 2.5 * loss + 2 * SIDE_COST
            units = int(min(cash / bar.open, .0075 * cash / loss))
            if units > 0:
                position = side, units, bar.open, bar.open - side * distance, bar.open + side * reward
        if position:
            side, units, entry, stop, target = position
            adverse, favorable = (bar.low, bar.high) if side > 0 else (bar.high, bar.low)
            fill = None
            if side * (bar.open - stop) <= 0:
                fill = bar.open
            elif side * (bar.open - target) >= 0:
                fill = target
            elif side * (adverse - stop) <= 0:
                fill = stop
            elif side * (favorable - target) >= 0:
                fill = target
            elif i == len(d) - 1:
                fill = bar.close
            if fill is not None:
                pnl = units * (side * (fill - entry) - 2 * SIDE_COST)
                trades.append((side, pnl))
                cash += pnl
                position = None
        equity = cash if position is None else cash + units * (side * (bar.close - entry) - 2 * SIDE_COST)
        peak = max(peak, equity)
        halted |= equity <= .9 * peak
        daily_halt |= equity <= .97 * day_start
    return (d.index[start], d.index[-1], sum(s > 0 for s, _ in trades),
            sum(s < 0 for s, _ in trades), cash - 200)


def main(dest):
    now = pd.Timestamp.now(tz="UTC")
    rows = ["# EUR/USD Forex trials", "", f"Historical paper replay updated {now:%Y-%m-%d %H:%M} UTC.",
            "", "| Strategy | Bars | First / last scored bar (UTC) | Longs | Shorts | Net P&L |",
            "|---|---|---|---:|---:|---:|"]
    for name, interval, span in SETUPS:
        first, last, longs, shorts, pnl = replay(name, fetch(interval, span, now))
        rows.append(f"| {name} | {interval} | {first:%Y-%m-%d %H:%M} / {last:%Y-%m-%d %H:%M} | "
                    f"{longs} | {shorts} | ${pnl:+.2f} |")
    rows += ["", "Each replay starts with $200 and scores the final 30% after indicator warmup. "
             "Signals use completed bars and enter at the next open. Results include a modeled "
             "1-pip spread and 0.1 pip slippage per side. Overnight financing is excluded.",
             "", "Hourly and 15-minute setups use a two-ATR stop and a net 2.5R target. "
             "Weekly large bodies exceed the 75th percentile of the preceding 20 bodies. "
             "The weekly trial uses 120 five-decimal points of risk and 60 points of reward in both directions. "
             "It is ineligible for the shared desk. When both levels fall within a bar, the stop wins.",
             "", "Source: Yahoo Finance EUR/USD indicative candles. Bar ranges include the observed open and close. Results are rolling historical tests. "
             "The crypto forward portfolio and its shortlist are tracked separately."]
    temp = dest.with_suffix(".tmp")
    temp.write_text("\n".join(rows) + "\n")
    temp.replace(dest)


if __name__ == "__main__":
    main(Path(sys.argv[1]))
