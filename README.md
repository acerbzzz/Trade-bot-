# Crypto paper desk

**Monitoring** · Kraken spot · 15-minute candles

Latest completed candle ended **2026-11-28 10:45 UTC**.

| Paper equity | Open positions | Closed trades |
|---:|---:|---:|
| $185.50 | 1 | 52 |

| Market | Last close | Trend | Mean reversion | Breakout | Momentum |
|---|---:|---|---|---|---|
| BTC/USD | $59,188.90 | Waiting | In position | Waiting | Waiting |
| ETH/USD | $1,647.78 | Waiting | Waiting | Waiting | Waiting |

## Strategy trials

One independent paper trial per worker minute. Net P&L includes modeled costs.

| Strategy | Closed | Realized P&L | Shortlisted | Next-day validation P&L |
|---|---:|---:|---|---:|
| trend | 13 | $-4.27 | Yes | $-0.28 |
| reversion | 27 | $-1.63 | Yes | $-0.18 |
| breakout | 19 | $-6.45 | Pending | — |
| momentum | 25 | $-10.08 | Yes | $+0.00 |
| relative_strength | 6 | $-3.72 | Pending | — |
| vwap_pullback | 45 | $-14.41 | Pending | — |
| failed_breakdown | 30 | $-10.29 | Yes | $-0.73 |
| grok_pullback | 26 | $-16.70 | Pending | — |
| grok_squeeze | 11 | $-7.90 | Pending | — |
| grok_supertrend | 15 | $+3.10 | Yes | $+0.00 |
| grok_stochastic | 12 | $-3.85 | Yes | $-2.19 |
| grok_confluence | 16 | $-0.44 | Yes | $+0.00 |

Relative strength trial equity: $196.28. 50/50 BTC–ETH buy-and-hold liquidation value: $178.87.

Validation leader: None profitable

Started with $200 simulated USD. Entries and exits are modeled from candles. No broker orders.

[Refresh history](https://github.com/acerbzzz/Trade-bot-/actions/workflows/forward-paper.yml)

Last successful market check: **2026-11-28 10:46 UTC** · Target interval: 1 minute.
Worker started: **2026-11-28 09:30 UTC** · [Worker run](https://github.com/acerbzzz/Trade-bot-/actions/runs/46130780672) · [Restored checkpoint](https://github.com/acerbzzz/Trade-bot-/commit/b208460a78e686b4639aefde5d35b42da51c8f2b)

[Open phone dashboard](https://ryans-paper-desk.enchantingchili2.chatgpt.site)
