# Crypto paper desk

**Monitoring** · Kraken spot · 15-minute candles

Latest completed candle ended **2026-11-17 16:30 UTC**.

| Paper equity | Open positions | Closed trades |
|---:|---:|---:|
| $197.09 | 0 | 6 |

| Market | Last close | Trend | Mean reversion | Breakout | Momentum |
|---|---:|---|---|---|---|
| BTC/USD | $63,836.70 | Waiting | Waiting | Waiting | Waiting |
| ETH/USD | $1,779.95 | Waiting | Waiting | Waiting | Waiting |

## Strategy trials

One independent paper trial per worker minute. Net P&L includes modeled costs.

| Strategy | Closed | Realized P&L | Shortlisted | Next-day validation P&L |
|---|---:|---:|---|---:|
| trend | 4 | $-4.73 | Pending | — |
| reversion | 6 | $+0.15 | Yes | — |
| breakout | 6 | $-5.28 | Pending | — |
| momentum | 6 | $-3.26 | Yes | $-1.70 |
| relative_strength | 1 | $-1.50 | Pending | — |
| vwap_pullback | 5 | $-3.66 | Pending | — |
| failed_breakdown | 9 | $+1.15 | Yes | — |
| grok_pullback | 6 | $-7.90 | Pending | — |
| grok_squeeze | 3 | $-2.89 | Pending | — |
| grok_supertrend | 4 | $-4.06 | Yes | $-1.13 |
| grok_stochastic | 1 | $-0.18 | Pending | — |
| grok_confluence | 4 | $-2.72 | Pending | — |

Relative strength trial equity: $198.50. 50/50 BTC–ETH buy-and-hold liquidation value: $192.70.

Validation leader: None profitable

Started with $200 simulated USD. Entries and exits are modeled from candles. No broker orders.

[Refresh history](https://github.com/acerbzzz/Trade-bot-/actions/workflows/forward-paper.yml)

Last successful market check: **2026-11-17 16:43 UTC** · Target interval: 1 minute.
Worker started: **2026-11-17 15:49 UTC** · [Worker run](https://github.com/acerbzzz/Trade-bot-/actions/runs/44118722300) · [Restored checkpoint](https://github.com/acerbzzz/Trade-bot-/commit/5990596f3ba47efb8452cb51f896040c6ad81e81)

[Open phone dashboard](https://ryans-paper-desk.enchantingchili2.chatgpt.site)
