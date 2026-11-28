# Crypto paper desk

**Monitoring** · Kraken spot · 15-minute candles

Latest completed candle ended **2026-11-28 08:30 UTC**.

| Paper equity | Open positions | Closed trades |
|---:|---:|---:|
| $185.94 | 0 | 52 |

| Market | Last close | Trend | Mean reversion | Breakout | Momentum |
|---|---:|---|---|---|---|
| BTC/USD | $59,611.70 | Waiting | Waiting | Waiting | Waiting |
| ETH/USD | $1,653.74 | Waiting | Waiting | Waiting | Waiting |

## Strategy trials

One independent paper trial per worker minute. Net P&L includes modeled costs.

| Strategy | Closed | Realized P&L | Shortlisted | Next-day validation P&L |
|---|---:|---:|---|---:|
| trend | 13 | $-4.27 | Yes | $-0.28 |
| reversion | 27 | $-1.63 | Yes | $-0.18 |
| breakout | 19 | $-6.45 | Pending | — |
| momentum | 25 | $-10.08 | Yes | $+0.00 |
| relative_strength | 6 | $-3.72 | Pending | — |
| vwap_pullback | 44 | $-13.68 | Pending | — |
| failed_breakdown | 30 | $-10.29 | Yes | $-0.73 |
| grok_pullback | 26 | $-16.70 | Pending | — |
| grok_squeeze | 11 | $-7.90 | Pending | — |
| grok_supertrend | 15 | $+3.10 | Yes | $+0.00 |
| grok_stochastic | 12 | $-3.85 | Yes | $-2.19 |
| grok_confluence | 16 | $-0.44 | Yes | $+0.00 |

Relative strength trial equity: $196.28. 50/50 BTC–ETH buy-and-hold liquidation value: $179.54.

Validation leader: None profitable

Started with $200 simulated USD. Entries and exits are modeled from candles. No broker orders.

[Refresh history](https://github.com/acerbzzz/Trade-bot-/actions/workflows/forward-paper.yml)

Last successful market check: **2026-11-28 08:34 UTC** · Target interval: 1 minute.
Worker started: **2026-11-28 08:00 UTC** · [Worker run](https://github.com/acerbzzz/Trade-bot-/actions/runs/46123765205) · [Restored checkpoint](https://github.com/acerbzzz/Trade-bot-/commit/19faf5801b4b50dba9b2e87c78fc00cbb49657f2)

[Open phone dashboard](https://ryans-paper-desk.enchantingchili2.chatgpt.site)
