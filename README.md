# Crypto paper desk

**Monitoring** · Kraken spot · 15-minute candles

Latest completed candle ended **2026-11-19 17:45 UTC**.

| Paper equity | Open positions | Closed trades |
|---:|---:|---:|
| $194.13 | 1 | 13 |

| Market | Last close | Trend | Mean reversion | Breakout | Momentum |
|---|---:|---|---|---|---|
| BTC/USD | $62,845.30 | Waiting | In position | Waiting | Waiting |
| ETH/USD | $1,772.38 | Waiting | Waiting | Waiting | Waiting |

## Strategy trials

One independent paper trial per worker minute. Net P&L includes modeled costs.

| Strategy | Closed | Realized P&L | Shortlisted | Next-day validation P&L |
|---|---:|---:|---|---:|
| trend | 6 | $-5.99 | Pending | — |
| reversion | 9 | $-2.00 | Yes | $-0.65 |
| breakout | 9 | $-6.35 | Pending | — |
| momentum | 9 | $-4.63 | Yes | $-0.33 |
| relative_strength | 2 | $-2.99 | Pending | — |
| vwap_pullback | 12 | $-6.40 | Pending | — |
| failed_breakdown | 12 | $-0.88 | Yes | $-1.44 |
| grok_pullback | 10 | $-10.46 | Pending | — |
| grok_squeeze | 5 | $-4.17 | Pending | — |
| grok_supertrend | 6 | $-6.84 | Yes | $+0.18 |
| grok_stochastic | 1 | $-0.18 | Pending | — |
| grok_confluence | 5 | $-2.50 | Pending | — |

Relative strength trial equity: $197.01. 50/50 BTC–ETH buy-and-hold liquidation value: $190.79.

Validation leader: grok_supertrend

Started with $200 simulated USD. Entries and exits are modeled from candles. No broker orders.

[Refresh history](https://github.com/acerbzzz/Trade-bot-/actions/workflows/forward-paper.yml)

Last successful market check: **2026-11-19 17:55 UTC** · Target interval: 1 minute.
Worker started: **2026-11-19 17:19 UTC** · [Worker run](https://github.com/acerbzzz/Trade-bot-/actions/runs/44575918936) · [Restored checkpoint](https://github.com/acerbzzz/Trade-bot-/commit/8fc44831ddc527461097402436e4ff15bab2da8e)

[Open phone dashboard](https://ryans-paper-desk.enchantingchili2.chatgpt.site)
