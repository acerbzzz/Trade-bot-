# Crypto paper desk

**Monitoring** · Kraken spot · 15-minute candles

Latest completed candle ended **2026-11-18 16:00 UTC**.

| Paper equity | Open positions | Closed trades |
|---:|---:|---:|
| $195.92 | 1 | 8 |

| Market | Last close | Trend | Mean reversion | Breakout | Momentum |
|---|---:|---|---|---|---|
| BTC/USD | $63,052.10 | Waiting | In position | Waiting | Waiting |
| ETH/USD | $1,767.04 | Waiting | Waiting | Waiting | Waiting |

## Strategy trials

One independent paper trial per worker minute. Net P&L includes modeled costs.

| Strategy | Closed | Realized P&L | Shortlisted | Next-day validation P&L |
|---|---:|---:|---|---:|
| trend | 4 | $-4.73 | Pending | — |
| reversion | 6 | $+0.15 | Yes | — |
| breakout | 8 | $-6.57 | Pending | — |
| momentum | 7 | $-3.58 | Yes | $-1.70 |
| relative_strength | 2 | $-2.99 | Pending | — |
| vwap_pullback | 10 | $-5.19 | Pending | — |
| failed_breakdown | 10 | $+0.56 | Yes | $-1.57 |
| grok_pullback | 7 | $-8.90 | Pending | — |
| grok_squeeze | 4 | $-2.77 | Pending | — |
| grok_supertrend | 5 | $-5.38 | Yes | $-2.89 |
| grok_stochastic | 1 | $-0.18 | Pending | — |
| grok_confluence | 4 | $-2.72 | Pending | — |

Relative strength trial equity: $197.01. 50/50 BTC–ETH buy-and-hold liquidation value: $190.82.

Validation leader: None profitable

Started with $200 simulated USD. Entries and exits are modeled from candles. No broker orders.

[Refresh history](https://github.com/acerbzzz/Trade-bot-/actions/workflows/forward-paper.yml)

Last successful market check: **2026-11-18 16:06 UTC** · Target interval: 1 minute.
Worker started: **2026-11-18 15:49 UTC** · [Worker run](https://github.com/acerbzzz/Trade-bot-/actions/runs/44340050603) · [Restored checkpoint](https://github.com/acerbzzz/Trade-bot-/commit/f8b141c0cdf0e7be69bb96a71fc9399c7bb871e7)

[Open phone dashboard](https://ryans-paper-desk.enchantingchili2.chatgpt.site)
