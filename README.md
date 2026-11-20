# Crypto paper desk

**Monitoring** · Kraken spot · 15-minute candles

Latest completed candle ended **2026-11-20 13:30 UTC**.

| Paper equity | Open positions | Closed trades |
|---:|---:|---:|
| $194.62 | 0 | 17 |

| Market | Last close | Trend | Mean reversion | Breakout | Momentum |
|---|---:|---|---|---|---|
| BTC/USD | $61,437.70 | Waiting | Waiting | Waiting | Waiting |
| ETH/USD | $1,731.26 | Waiting | Waiting | Waiting | Waiting |

## Strategy trials

One independent paper trial per worker minute. Net P&L includes modeled costs.

| Strategy | Closed | Realized P&L | Shortlisted | Next-day validation P&L |
|---|---:|---:|---|---:|
| trend | 6 | $-5.99 | Pending | — |
| reversion | 12 | $+0.93 | Yes | $+0.94 |
| breakout | 10 | $-7.80 | Pending | — |
| momentum | 9 | $-4.63 | Yes | $-1.07 |
| relative_strength | 2 | $-2.99 | Pending | — |
| vwap_pullback | 15 | $-8.69 | Pending | — |
| failed_breakdown | 14 | $-2.83 | Yes | $-0.56 |
| grok_pullback | 10 | $-10.46 | Pending | — |
| grok_squeeze | 6 | $-5.64 | Pending | — |
| grok_supertrend | 7 | $-8.28 | Yes | $+0.00 |
| grok_stochastic | 1 | $-0.18 | Pending | — |
| grok_confluence | 5 | $-2.50 | Pending | — |

Relative strength trial equity: $197.01. 50/50 BTC–ETH buy-and-hold liquidation value: $186.44.

Validation leader: reversion

Started with $200 simulated USD. Entries and exits are modeled from candles. No broker orders.

[Refresh history](https://github.com/acerbzzz/Trade-bot-/actions/workflows/forward-paper.yml)

Last successful market check: **2026-11-20 13:37 UTC** · Target interval: 1 minute.
Worker started: **2026-11-20 12:49 UTC** · [Worker run](https://github.com/acerbzzz/Trade-bot-/actions/runs/44738996266) · [Restored checkpoint](https://github.com/acerbzzz/Trade-bot-/commit/b4888baf1bdd738173767ff60877945b0c10313c)

[Open phone dashboard](https://ryans-paper-desk.enchantingchili2.chatgpt.site)
