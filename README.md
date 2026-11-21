# Crypto paper desk

**Monitoring** · Kraken spot · 15-minute candles

Latest completed candle ended **2026-11-21 03:15 UTC**.

| Paper equity | Open positions | Closed trades |
|---:|---:|---:|
| $190.28 | 0 | 20 |

| Market | Last close | Trend | Mean reversion | Breakout | Momentum |
|---|---:|---|---|---|---|
| BTC/USD | $58,380.90 | Waiting | Waiting | Waiting | Waiting |
| ETH/USD | $1,612.48 | Waiting | Waiting | Waiting | Waiting |

## Strategy trials

One independent paper trial per worker minute. Net P&L includes modeled costs.

| Strategy | Closed | Realized P&L | Shortlisted | Next-day validation P&L |
|---|---:|---:|---|---:|
| trend | 6 | $-5.99 | Pending | — |
| reversion | 14 | $-2.06 | Yes | $-2.49 |
| breakout | 10 | $-7.80 | Pending | — |
| momentum | 10 | $-6.10 | Yes | $-1.50 |
| relative_strength | 2 | $-2.99 | Pending | — |
| vwap_pullback | 19 | $-10.86 | Pending | — |
| failed_breakdown | 17 | $-4.82 | Yes | $-1.59 |
| grok_pullback | 10 | $-10.46 | Pending | — |
| grok_squeeze | 6 | $-5.64 | Pending | — |
| grok_supertrend | 8 | $-9.71 | Yes | $-2.12 |
| grok_stochastic | 1 | $-0.18 | Pending | — |
| grok_confluence | 5 | $-2.50 | Pending | — |

Relative strength trial equity: $197.01. 50/50 BTC–ETH buy-and-hold liquidation value: $175.85.

Validation leader: None profitable

Started with $200 simulated USD. Entries and exits are modeled from candles. No broker orders.

[Refresh history](https://github.com/acerbzzz/Trade-bot-/actions/workflows/forward-paper.yml)

Last successful market check: **2026-11-21 03:19 UTC** · Target interval: 1 minute.
Worker started: **2026-11-21 02:19 UTC** · [Worker run](https://github.com/acerbzzz/Trade-bot-/actions/runs/44853942113) · [Restored checkpoint](https://github.com/acerbzzz/Trade-bot-/commit/76a216c3f741386729f8f000a4289a988b3216e7)

[Open phone dashboard](https://ryans-paper-desk.enchantingchili2.chatgpt.site)
