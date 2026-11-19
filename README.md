# Crypto paper desk

**Monitoring** · Kraken spot · 15-minute candles

Latest completed candle ended **2026-11-19 16:00 UTC**.

| Paper equity | Open positions | Closed trades |
|---:|---:|---:|
| $195.06 | 1 | 12 |

| Market | Last close | Trend | Mean reversion | Breakout | Momentum |
|---|---:|---|---|---|---|
| BTC/USD | $63,028.90 | Waiting | In position | Waiting | Waiting |
| ETH/USD | $1,780.49 | Waiting | Waiting | Waiting | Waiting |

## Strategy trials

One independent paper trial per worker minute. Net P&L includes modeled costs.

| Strategy | Closed | Realized P&L | Shortlisted | Next-day validation P&L |
|---|---:|---:|---|---:|
| trend | 6 | $-5.99 | Pending | — |
| reversion | 8 | $-0.51 | Yes | $-0.65 |
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

Relative strength trial equity: $197.01. 50/50 BTC–ETH buy-and-hold liquidation value: $191.51.

Validation leader: grok_supertrend

Started with $200 simulated USD. Entries and exits are modeled from candles. No broker orders.

[Refresh history](https://github.com/acerbzzz/Trade-bot-/actions/workflows/forward-paper.yml)

Last successful market check: **2026-11-19 16:13 UTC** · Target interval: 1 minute.
Worker started: **2026-11-19 15:49 UTC** · [Worker run](https://github.com/acerbzzz/Trade-bot-/actions/runs/44559132494) · [Restored checkpoint](https://github.com/acerbzzz/Trade-bot-/commit/bfd818939e572f259ab5cb689a7fe8d80b4b2359)

[Open phone dashboard](https://ryans-paper-desk.enchantingchili2.chatgpt.site)
