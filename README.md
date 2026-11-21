# Crypto paper desk

**Monitoring** · Kraken spot · 15-minute candles

Latest completed candle ended **2026-11-21 05:15 UTC**.

| Paper equity | Open positions | Closed trades |
|---:|---:|---:|
| $189.40 | 1 | 21 |

| Market | Last close | Trend | Mean reversion | Breakout | Momentum |
|---|---:|---|---|---|---|
| BTC/USD | $56,241.40 | Waiting | In position | Waiting | Waiting |
| ETH/USD | $1,564.42 | Waiting | Waiting | Waiting | Waiting |

## Strategy trials

One independent paper trial per worker minute. Net P&L includes modeled costs.

| Strategy | Closed | Realized P&L | Shortlisted | Next-day validation P&L |
|---|---:|---:|---|---:|
| trend | 6 | $-5.99 | Pending | — |
| reversion | 15 | $-3.54 | Yes | $-2.49 |
| breakout | 10 | $-7.80 | Pending | — |
| momentum | 10 | $-6.10 | Yes | $-1.50 |
| relative_strength | 2 | $-2.99 | Pending | — |
| vwap_pullback | 19 | $-10.86 | Pending | — |
| failed_breakdown | 19 | $-7.73 | Yes | $-1.59 |
| grok_pullback | 10 | $-10.46 | Pending | — |
| grok_squeeze | 6 | $-5.64 | Pending | — |
| grok_supertrend | 8 | $-9.71 | Yes | $-2.12 |
| grok_stochastic | 1 | $-0.18 | Pending | — |
| grok_confluence | 5 | $-2.50 | Pending | — |

Relative strength trial equity: $197.01. 50/50 BTC–ETH buy-and-hold liquidation value: $169.57.

Validation leader: None profitable

Started with $200 simulated USD. Entries and exits are modeled from candles. No broker orders.

[Refresh history](https://github.com/acerbzzz/Trade-bot-/actions/workflows/forward-paper.yml)

Last successful market check: **2026-11-21 05:28 UTC** · Target interval: 1 minute.
Worker started: **2026-11-21 05:19 UTC** · [Worker run](https://github.com/acerbzzz/Trade-bot-/actions/runs/44870341107) · [Restored checkpoint](https://github.com/acerbzzz/Trade-bot-/commit/b2809a56426d71f042afed1ce590d1b447843641)

[Open phone dashboard](https://ryans-paper-desk.enchantingchili2.chatgpt.site)
