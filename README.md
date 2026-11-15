# Crypto paper desk

**Monitoring** · Kraken spot · 15-minute candles

Latest completed candle ended **2026-11-15 20:00 UTC**.

| Paper equity | Open positions | Closed trades |
|---:|---:|---:|
| $199.32 | 1 | 1 |

| Market | Last close | Trend | Mean reversion | Breakout | Momentum |
|---|---:|---|---|---|---|
| BTC/USD | $64,907.30 | Waiting | Waiting | Waiting | In position |
| ETH/USD | $1,823.25 | Waiting | Waiting | Waiting | Waiting |

## Strategy trials

One independent paper trial per worker minute. Net P&L includes modeled costs.

| Strategy | Closed | Realized P&L | Shortlisted | Next-day validation P&L |
|---|---:|---:|---|---:|
| trend | 2 | $-1.78 | Pending | — |
| reversion | 5 | $-1.56 | Pending | — |
| breakout | 2 | $-0.49 | Pending | — |
| momentum | 1 | $+0.06 | Yes | — |
| relative_strength | 0 | $+0.00 | Pending | — |
| vwap_pullback | 0 | $+0.00 | Pending | — |
| failed_breakdown | 6 | $-0.60 | Pending | — |
| grok_pullback | 2 | $-2.05 | Pending | — |
| grok_squeeze | 0 | $+0.00 | Pending | — |
| grok_supertrend | 1 | $+0.04 | Yes | — |
| grok_stochastic | 0 | $+0.00 | Pending | — |
| grok_confluence | 2 | $-0.59 | Pending | — |

Relative strength trial equity: $200.00. 50/50 BTC–ETH buy-and-hold liquidation value: $196.66.

Started with $200 simulated USD. Entries and exits are modeled from candles. No broker orders.

[Refresh history](https://github.com/acerbzzz/Trade-bot-/actions/workflows/forward-paper.yml)

Last successful market check: **2026-11-15 20:02 UTC** · Target interval: 1 minute.
