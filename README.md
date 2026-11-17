# Crypto paper desk

**Monitoring** · Kraken spot · 15-minute candles

Latest completed candle ended **2026-11-17 06:30 UTC**.

| Paper equity | Open positions | Closed trades |
|---:|---:|---:|
| $196.79 | 1 | 3 |

| Market | Last close | Trend | Mean reversion | Breakout | Momentum |
|---|---:|---|---|---|---|
| BTC/USD | $64,532.40 | Waiting | Waiting | Waiting | Waiting |
| ETH/USD | $1,827.34 | Waiting | Waiting | In position | Waiting |

## Strategy trials

One independent paper trial per worker minute. Net P&L includes modeled costs.

| Strategy | Closed | Realized P&L | Shortlisted | Next-day validation P&L |
|---|---:|---:|---|---:|
| trend | 3 | $-3.26 | Pending | — |
| reversion | 5 | $-1.56 | Pending | — |
| breakout | 4 | $-2.81 | Pending | — |
| momentum | 5 | $-2.29 | Yes | $-1.70 |
| relative_strength | 1 | $-1.50 | Pending | — |
| vwap_pullback | 3 | $-2.50 | Pending | — |
| failed_breakdown | 8 | $+2.15 | Yes | — |
| grok_pullback | 4 | $-4.99 | Pending | — |
| grok_squeeze | 3 | $-2.89 | Pending | — |
| grok_supertrend | 2 | $-1.09 | Yes | $-1.13 |
| grok_stochastic | 1 | $-0.18 | Pending | — |
| grok_confluence | 3 | $-1.71 | Pending | — |

Relative strength trial equity: $198.50. 50/50 BTC–ETH buy-and-hold liquidation value: $196.76.

Validation leader: None profitable

Started with $200 simulated USD. Entries and exits are modeled from candles. No broker orders.

[Refresh history](https://github.com/acerbzzz/Trade-bot-/actions/workflows/forward-paper.yml)

Last successful market check: **2026-11-17 06:33 UTC** · Target interval: 1 minute.
Worker started: **2026-11-17 05:18 UTC** · [Worker run](https://github.com/acerbzzz/Trade-bot-/actions/runs/44013490430) · [Restored checkpoint](https://github.com/acerbzzz/Trade-bot-/commit/bd35d39bf5a3736a69d88cfc9ada1b3ffcacb2f7)

[Open phone dashboard](https://ryans-paper-desk.enchantingchili2.chatgpt.site)
