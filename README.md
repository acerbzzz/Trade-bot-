# Crypto paper desk

**Monitoring** · Kraken spot · 15-minute candles

Latest completed candle ended **2026-11-22 10:15 UTC**.

| Paper equity | Open positions | Closed trades |
|---:|---:|---:|
| $194.13 | 1 | 27 |

| Market | Last close | Trend | Mean reversion | Breakout | Momentum |
|---|---:|---|---|---|---|
| BTC/USD | $60,934.10 | Waiting | Waiting | In position | Waiting |
| ETH/USD | $1,710.73 | Waiting | Waiting | Waiting | Waiting |

## Strategy trials

One independent paper trial per worker minute. Net P&L includes modeled costs.

| Strategy | Closed | Realized P&L | Shortlisted | Next-day validation P&L |
|---|---:|---:|---|---:|
| trend | 8 | $-3.19 | Pending | — |
| reversion | 18 | $-4.62 | Yes | $+0.35 |
| breakout | 12 | $-2.66 | Pending | — |
| momentum | 11 | $-2.47 | Yes | $+3.74 |
| relative_strength | 3 | $-4.41 | Pending | — |
| vwap_pullback | 21 | $-3.71 | Pending | — |
| failed_breakdown | 20 | $-4.14 | Yes | $+2.21 |
| grok_pullback | 13 | $-7.73 | Pending | — |
| grok_squeeze | 7 | $-3.83 | Pending | — |
| grok_supertrend | 10 | $-2.52 | Yes | $+3.75 |
| grok_stochastic | 2 | $-0.32 | Pending | — |
| grok_confluence | 7 | $+4.97 | Yes | — |

Relative strength trial equity: $195.59. 50/50 BTC–ETH buy-and-hold liquidation value: $184.94.

Validation leader: grok_supertrend

Started with $200 simulated USD. Entries and exits are modeled from candles. No broker orders.

[Refresh history](https://github.com/acerbzzz/Trade-bot-/actions/workflows/forward-paper.yml)

Last successful market check: **2026-11-22 10:22 UTC** · Target interval: 1 minute.
Worker started: **2026-11-22 09:49 UTC** · [Worker run](https://github.com/acerbzzz/Trade-bot-/actions/runs/45005005353) · [Restored checkpoint](https://github.com/acerbzzz/Trade-bot-/commit/37eb008e18f41f1db5fd9c955b201c06c633799c)

[Open phone dashboard](https://ryans-paper-desk.enchantingchili2.chatgpt.site)
