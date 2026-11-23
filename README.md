# Crypto paper desk

**Monitoring** · Kraken spot · 15-minute candles

Latest completed candle ended **2026-11-23 07:45 UTC**.

| Paper equity | Open positions | Closed trades |
|---:|---:|---:|
| $190.74 | 1 | 31 |

| Market | Last close | Trend | Mean reversion | Breakout | Momentum |
|---|---:|---|---|---|---|
| BTC/USD | $61,406.60 | In position | Waiting | Waiting | Waiting |
| ETH/USD | $1,720.34 | Waiting | Waiting | Waiting | Waiting |

## Strategy trials

One independent paper trial per worker minute. Net P&L includes modeled costs.

| Strategy | Closed | Realized P&L | Shortlisted | Next-day validation P&L |
|---|---:|---:|---|---:|
| trend | 9 | $+0.47 | Yes | — |
| reversion | 18 | $-4.62 | Yes | $-2.91 |
| breakout | 14 | $-4.49 | Pending | — |
| momentum | 14 | $-5.12 | Yes | $-2.15 |
| relative_strength | 4 | $-5.87 | Pending | — |
| vwap_pullback | 22 | $-4.64 | Pending | — |
| failed_breakdown | 20 | $-4.14 | Yes | $+0.00 |
| grok_pullback | 17 | $-9.81 | Pending | — |
| grok_squeeze | 9 | $-5.95 | Pending | — |
| grok_supertrend | 10 | $-2.52 | Yes | $+3.75 |
| grok_stochastic | 5 | $+0.64 | Yes | — |
| grok_confluence | 7 | $+4.97 | Yes | $+3.74 |

Relative strength trial equity: $194.13. 50/50 BTC–ETH buy-and-hold liquidation value: $185.81.

Validation leader: grok_supertrend

Started with $200 simulated USD. Entries and exits are modeled from candles. No broker orders.

[Refresh history](https://github.com/acerbzzz/Trade-bot-/actions/workflows/forward-paper.yml)

Last successful market check: **2026-11-23 07:51 UTC** · Target interval: 1 minute.
Worker started: **2026-11-23 07:03 UTC** · [Worker run](https://github.com/acerbzzz/Trade-bot-/actions/runs/45128358491) · [Restored checkpoint](https://github.com/acerbzzz/Trade-bot-/commit/eddb8e8ba2bb606dbc1f438fe71302d10d80b195)

[Open phone dashboard](https://ryans-paper-desk.enchantingchili2.chatgpt.site)
