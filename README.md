# Crypto paper desk

**Monitoring** · Kraken spot · 15-minute candles

Latest completed candle ended **2026-11-16 21:15 UTC**.

| Paper equity | Open positions | Closed trades |
|---:|---:|---:|
| $198.62 | 0 | 2 |

| Market | Last close | Trend | Mean reversion | Breakout | Momentum |
|---|---:|---|---|---|---|
| BTC/USD | $64,992.20 | Waiting | Waiting | Waiting | Waiting |
| ETH/USD | $1,819.21 | Waiting | Waiting | Waiting | Waiting |

## Strategy trials

One independent paper trial per worker minute. Net P&L includes modeled costs.

| Strategy | Closed | Realized P&L | Shortlisted | Next-day validation P&L |
|---|---:|---:|---|---:|
| trend | 3 | $-3.26 | Pending | — |
| reversion | 5 | $-1.56 | Pending | — |
| breakout | 2 | $-0.49 | Pending | — |
| momentum | 3 | $-1.64 | Yes | — |
| relative_strength | 1 | $-1.50 | Pending | — |
| vwap_pullback | 1 | $-0.71 | Pending | — |
| failed_breakdown | 6 | $-0.60 | Pending | — |
| grok_pullback | 2 | $-2.05 | Pending | — |
| grok_squeeze | 2 | $-1.71 | Pending | — |
| grok_supertrend | 2 | $-1.09 | Yes | — |
| grok_stochastic | 1 | $-0.18 | Pending | — |
| grok_confluence | 3 | $-1.71 | Pending | — |

Relative strength trial equity: $198.50. 50/50 BTC–ETH buy-and-hold liquidation value: $195.23.

Started with $200 simulated USD. Entries and exits are modeled from candles. No broker orders.

[Refresh history](https://github.com/acerbzzz/Trade-bot-/actions/workflows/forward-paper.yml)

Last successful market check: **2026-11-16 21:18 UTC** · Target interval: 1 minute.
