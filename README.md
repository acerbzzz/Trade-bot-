# Crypto paper desk

**Monitoring** · Kraken spot · 15-minute candles

Latest completed candle ended **2026-11-22 02:45 UTC**.

| Paper equity | Open positions | Closed trades |
|---:|---:|---:|
| $193.66 | 0 | 24 |

| Market | Last close | Trend | Mean reversion | Breakout | Momentum |
|---|---:|---|---|---|---|
| BTC/USD | $59,499.50 | Waiting | Entry signal | Waiting | Waiting |
| ETH/USD | $1,667.95 | Waiting | Entry signal | Waiting | Waiting |

## Strategy trials

One independent paper trial per worker minute. Net P&L includes modeled costs.

| Strategy | Closed | Realized P&L | Shortlisted | Next-day validation P&L |
|---|---:|---:|---|---:|
| trend | 6 | $-5.99 | Pending | — |
| reversion | 16 | $-1.73 | Yes | $+0.35 |
| breakout | 11 | $-6.28 | Pending | — |
| momentum | 11 | $-2.47 | Yes | $+3.74 |
| relative_strength | 3 | $-4.41 | Pending | — |
| vwap_pullback | 20 | $-7.32 | Pending | — |
| failed_breakdown | 20 | $-4.14 | Yes | $+2.21 |
| grok_pullback | 13 | $-7.73 | Pending | — |
| grok_squeeze | 7 | $-3.83 | Pending | — |
| grok_supertrend | 9 | $-6.16 | Yes | $+3.75 |
| grok_stochastic | 2 | $-0.32 | Pending | — |
| grok_confluence | 6 | $+1.20 | Yes | — |

Relative strength trial equity: $195.59. 50/50 BTC–ETH buy-and-hold liquidation value: $180.09.

Validation leader: grok_supertrend

Started with $200 simulated USD. Entries and exits are modeled from candles. No broker orders.

[Refresh history](https://github.com/acerbzzz/Trade-bot-/actions/workflows/forward-paper.yml)

Last successful market check: **2026-11-22 02:53 UTC** · Target interval: 1 minute.
Worker started: **2026-11-22 02:19 UTC** · [Worker run](https://github.com/acerbzzz/Trade-bot-/actions/runs/44973374978) · [Restored checkpoint](https://github.com/acerbzzz/Trade-bot-/commit/41da0277e4c8d1e1974bbe24b695b405fdc9dca3)

[Open phone dashboard](https://ryans-paper-desk.enchantingchili2.chatgpt.site)
