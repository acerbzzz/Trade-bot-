# Crypto paper desk

**Monitoring** · Kraken spot · 15-minute candles

Latest completed candle ended **2026-11-28 15:45 UTC**.

| Paper equity | Open positions | Closed trades |
|---:|---:|---:|
| $185.42 | 0 | 54 |

| Market | Last close | Trend | Mean reversion | Breakout | Momentum |
|---|---:|---|---|---|---|
| BTC/USD | $59,261.80 | Waiting | Waiting | Waiting | Waiting |
| ETH/USD | $1,644.74 | Waiting | Waiting | Waiting | Waiting |

## Strategy trials

One independent paper trial per worker minute. Net P&L includes modeled costs.

| Strategy | Closed | Realized P&L | Shortlisted | Next-day validation P&L |
|---|---:|---:|---|---:|
| trend | 13 | $-4.27 | Yes | $-0.28 |
| reversion | 29 | $-2.18 | Yes | $-0.18 |
| breakout | 19 | $-6.45 | Pending | — |
| momentum | 25 | $-10.08 | Yes | $+0.00 |
| relative_strength | 6 | $-3.72 | Pending | — |
| vwap_pullback | 45 | $-14.41 | Pending | — |
| failed_breakdown | 31 | $-11.48 | Yes | $-0.73 |
| grok_pullback | 26 | $-16.70 | Pending | — |
| grok_squeeze | 11 | $-7.90 | Pending | — |
| grok_supertrend | 15 | $+3.10 | Yes | $+0.00 |
| grok_stochastic | 12 | $-3.85 | Yes | $-2.19 |
| grok_confluence | 16 | $-0.44 | Yes | $+0.00 |

Relative strength trial equity: $196.28. 50/50 BTC–ETH buy-and-hold liquidation value: $178.48.

Validation leader: None profitable

Started with $200 simulated USD. Entries and exits are modeled from candles. No broker orders.

[Refresh history](https://github.com/acerbzzz/Trade-bot-/actions/workflows/forward-paper.yml)

Last successful market check: **2026-11-28 15:59 UTC** · Target interval: 1 minute.
Worker started: **2026-11-28 15:30 UTC** · [Worker run](https://github.com/acerbzzz/Trade-bot-/actions/runs/46160209859) · [Restored checkpoint](https://github.com/acerbzzz/Trade-bot-/commit/92ce6dfa3ba9b5f8b8c91fbcd7a1fa923cac7c0f)

[Open phone dashboard](https://ryans-paper-desk.enchantingchili2.chatgpt.site)
