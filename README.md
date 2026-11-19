# Crypto paper desk

**Monitoring** · Kraken spot · 15-minute candles

Latest completed candle ended **2026-11-19 13:45 UTC**.

| Paper equity | Open positions | Closed trades |
|---:|---:|---:|
| $195.56 | 1 | 11 |

| Market | Last close | Trend | Mean reversion | Breakout | Momentum |
|---|---:|---|---|---|---|
| BTC/USD | $63,659.80 | In position | Waiting | Waiting | Waiting |
| ETH/USD | $1,803.92 | Waiting | Waiting | Waiting | Waiting |

## Strategy trials

One independent paper trial per worker minute. Net P&L includes modeled costs.

| Strategy | Closed | Realized P&L | Shortlisted | Next-day validation P&L |
|---|---:|---:|---|---:|
| trend | 5 | $-6.19 | Pending | — |
| reversion | 8 | $-0.51 | Yes | $-0.65 |
| breakout | 9 | $-6.35 | Pending | — |
| momentum | 8 | $-3.16 | Yes | $-0.33 |
| relative_strength | 2 | $-2.99 | Pending | — |
| vwap_pullback | 12 | $-6.40 | Pending | — |
| failed_breakdown | 12 | $-0.88 | Yes | $-1.44 |
| grok_pullback | 8 | $-8.87 | Pending | — |
| grok_squeeze | 4 | $-2.77 | Pending | — |
| grok_supertrend | 6 | $-6.84 | Yes | $+0.18 |
| grok_stochastic | 1 | $-0.18 | Pending | — |
| grok_confluence | 5 | $-2.50 | Pending | — |

Relative strength trial equity: $197.01. 50/50 BTC–ETH buy-and-hold liquidation value: $193.73.

Validation leader: grok_supertrend

Started with $200 simulated USD. Entries and exits are modeled from candles. No broker orders.

[Refresh history](https://github.com/acerbzzz/Trade-bot-/actions/workflows/forward-paper.yml)

Last successful market check: **2026-11-19 13:57 UTC** · Target interval: 1 minute.
Worker started: **2026-11-19 12:49 UTC** · [Worker run](https://github.com/acerbzzz/Trade-bot-/actions/runs/44527465352) · [Restored checkpoint](https://github.com/acerbzzz/Trade-bot-/commit/adb976c9e28e2f3013779b5ea8b889141d2b0d5d)

[Open phone dashboard](https://ryans-paper-desk.enchantingchili2.chatgpt.site)
