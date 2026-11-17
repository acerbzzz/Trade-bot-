# Crypto paper desk

**Monitoring** · Kraken spot · 15-minute candles

Latest completed candle ended **2026-11-17 14:30 UTC**.

| Paper equity | Open positions | Closed trades |
|---:|---:|---:|
| $198.10 | 1 | 5 |

| Market | Last close | Trend | Mean reversion | Breakout | Momentum |
|---|---:|---|---|---|---|
| BTC/USD | $64,861.90 | Waiting | Waiting | In position | Waiting |
| ETH/USD | $1,820.44 | Waiting | Waiting | Waiting | Waiting |

## Strategy trials

One independent paper trial per worker minute. Net P&L includes modeled costs.

| Strategy | Closed | Realized P&L | Shortlisted | Next-day validation P&L |
|---|---:|---:|---|---:|
| trend | 3 | $-3.26 | Pending | — |
| reversion | 6 | $+0.15 | Yes | — |
| breakout | 5 | $-4.28 | Pending | — |
| momentum | 6 | $-3.26 | Yes | $-1.70 |
| relative_strength | 1 | $-1.50 | Pending | — |
| vwap_pullback | 4 | $-3.17 | Pending | — |
| failed_breakdown | 8 | $+2.15 | Yes | — |
| grok_pullback | 5 | $-6.45 | Pending | — |
| grok_squeeze | 3 | $-2.89 | Pending | — |
| grok_supertrend | 3 | $-2.58 | Yes | $-1.13 |
| grok_stochastic | 1 | $-0.18 | Pending | — |
| grok_confluence | 3 | $-1.71 | Pending | — |

Relative strength trial equity: $198.50. 50/50 BTC–ETH buy-and-hold liquidation value: $196.75.

Validation leader: None profitable

Started with $200 simulated USD. Entries and exits are modeled from candles. No broker orders.

[Refresh history](https://github.com/acerbzzz/Trade-bot-/actions/workflows/forward-paper.yml)

Last successful market check: **2026-11-17 14:35 UTC** · Target interval: 1 minute.
Worker started: **2026-11-17 14:19 UTC** · [Worker run](https://github.com/acerbzzz/Trade-bot-/actions/runs/44101835446) · [Restored checkpoint](https://github.com/acerbzzz/Trade-bot-/commit/6b4c337171712779e7178e11e7c363e3e2a1006f)

[Open phone dashboard](https://ryans-paper-desk.enchantingchili2.chatgpt.site)
