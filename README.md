# Crypto paper desk

**Monitoring** · Kraken spot · 15-minute candles

Latest completed candle ended **2026-11-18 23:30 UTC**.

| Paper equity | Open positions | Closed trades |
|---:|---:|---:|
| $195.93 | 0 | 10 |

| Market | Last close | Trend | Mean reversion | Breakout | Momentum |
|---|---:|---|---|---|---|
| BTC/USD | $62,693.90 | Waiting | Waiting | Waiting | Waiting |
| ETH/USD | $1,770.86 | Waiting | Waiting | Waiting | Waiting |

## Strategy trials

One independent paper trial per worker minute. Net P&L includes modeled costs.

| Strategy | Closed | Realized P&L | Shortlisted | Next-day validation P&L |
|---|---:|---:|---|---:|
| trend | 4 | $-4.73 | Pending | — |
| reversion | 8 | $-0.51 | Yes | — |
| breakout | 8 | $-6.57 | Pending | — |
| momentum | 7 | $-3.58 | Yes | $-1.70 |
| relative_strength | 2 | $-2.99 | Pending | — |
| vwap_pullback | 10 | $-5.19 | Pending | — |
| failed_breakdown | 12 | $-0.88 | Yes | $-1.57 |
| grok_pullback | 7 | $-8.90 | Pending | — |
| grok_squeeze | 4 | $-2.77 | Pending | — |
| grok_supertrend | 5 | $-5.38 | Yes | $-2.89 |
| grok_stochastic | 1 | $-0.18 | Pending | — |
| grok_confluence | 4 | $-2.72 | Pending | — |

Relative strength trial equity: $197.01. 50/50 BTC–ETH buy-and-hold liquidation value: $190.48.

Validation leader: None profitable

Started with $200 simulated USD. Entries and exits are modeled from candles. No broker orders.

[Refresh history](https://github.com/acerbzzz/Trade-bot-/actions/workflows/forward-paper.yml)

Last successful market check: **2026-11-18 23:37 UTC** · Target interval: 1 minute.
Worker started: **2026-11-18 23:19 UTC** · [Worker run](https://github.com/acerbzzz/Trade-bot-/actions/runs/44419730320) · [Restored checkpoint](https://github.com/acerbzzz/Trade-bot-/commit/8a16420c9cdd9486f0f1e26216a7be3c7230903d)

[Open phone dashboard](https://ryans-paper-desk.enchantingchili2.chatgpt.site)
