"""Experimental signals for independent Kraken paper trials. Index is candle open (UTC)."""
import pandas as pd

BAR = pd.Timedelta(minutes=15)


def add_signals(frames):
    closes = pd.concat({s: d.close for s, d in frames.items()}, axis=1)
    daily_returns = closes / closes.shift(freq="1D").reindex(closes.index) - 1
    valid = daily_returns.notna().all(axis=1)
    # A tied daily ranking stays in cash.
    leaders = daily_returns.rank(axis=1, ascending=False, method="min") == 1
    decision = (closes.index + BAR) == (closes.index + BAR).normalize()
    for symbol, d in frames.items():
        winner = leaders[symbol] & (leaders.sum(axis=1) == 1) & (daily_returns[symbol] > 0)
        d["relative_strength_enter"] = valid & decision & winner
        d["relative_strength_exit"] = valid & decision & ~winner

        day = d.index.normalize()
        volume = d.volume.groupby(day).cumsum()
        vwap = (d.bar_vwap * d.volume).groupby(day).cumsum() / volume.where(volume > 0)
        # Compare the two latest completed hourly closes; no unfinished hour is used.
        hourly = d.close[d.index.minute == 45]
        rising = (hourly > hourly.shift(freq="1h").reindex(hourly.index)).reindex(d.index, method="ffill")
        same_day = day.to_series(index=d.index).eq(day.to_series(index=d.index).shift())
        d["vwap_pullback_enter"] = (rising.eq(True) & same_day &
                                    (d.close.shift() < vwap.shift()) & (d.close > vwap))
        d["vwap_pullback_exit"] = d.close < vwap
        floor = d.low.shift().rolling(96).min()
        d["failed_breakdown_level"] = floor
        d["failed_breakdown_enter"] = (d.low < floor) & (d.close > floor)
        d["failed_breakdown_exit"] = False  # Set against the position's saved level.
