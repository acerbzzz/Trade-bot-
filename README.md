# Crypto paper desk

**Monitoring** · Kraken spot · 15-minute candles

Latest completed candle ended **2026-11-19 22:45 UTC**.

| Paper equity | Open positions | Closed trades |
|---:|---:|---:|
| $196.01 | 1 | 14 |

| Market | Last close | Trend | Mean reversion | Breakout | Momentum |
|---|---:|---|---|---|---|
| BTC/USD | $62,175.00 | Waiting | In position | Waiting | Waiting |
| ETH/USD | $1,761.70 | Waiting | Waiting | Waiting | Waiting |

## Strategy trials

One independent paper trial per worker minute. Net P&L includes modeled costs.

| Strategy | Closed | Realized P&L | Shortlisted | Next-day validation P&L |
|---|---:|---:|---|---:|
| trend | 6 | $-5.99 | Pending | — |
| reversion | 10 | $-0.40 | Yes | $-0.65 |
| breakout | 9 | $-6.35 | Pending | — |
| momentum | 9 | $-4.63 | Yes | $-0.33 |
| relative_strength | 2 | $-2.99 | Pending | — |
| vwap_pullback | 12 | $-6.40 | Pending | — |
| failed_breakdown | 13 | $-2.20 | Yes | $-1.44 |
| grok_pullback | 10 | $-10.46 | Pending | — |
| grok_squeeze | 5 | $-4.17 | Pending | — |
| grok_supertrend | 6 | $-6.84 | Yes | $+0.18 |
| grok_stochastic | 1 | $-0.18 | Pending | — |
| grok_confluence | 5 | $-2.50 | Pending | — |

Relative strength trial equity: $197.01. 50/50 BTC–ETH buy-and-hold liquidation value: $189.20.

Validation leader: grok_supertrend

Started with $200 simulated USD. Entries and exits are modeled from candles. No broker orders.

[Refresh history](https://github.com/acerbzzz/Trade-bot-/actions/workflows/forward-paper.yml)

Last successful market check: **2026-11-19 22:59 UTC** · Target interval: 1 minute.
Worker started: **2026-11-19 21:49 UTC** · [Worker run](https://github.com/acerbzzz/Trade-bot-/actions/runs/44622608529) · [Restored checkpoint](https://github.com/acerbzzz/Trade-bot-/commit/95de7e05a8320376e51d8bcbfe1c4658363d5668)

[Open phone dashboard](https://ryans-paper-desk.enchantingchili2.chatgpt.site)
