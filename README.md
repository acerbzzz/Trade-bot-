# Crypto paper desk

**Monitoring** · Kraken spot · 15-minute candles

Latest completed candle ended **2026-11-23 00:30 UTC**.

| Paper equity | Open positions | Closed trades |
|---:|---:|---:|
| $191.48 | 1 | 30 |

| Market | Last close | Trend | Mean reversion | Breakout | Momentum |
|---|---:|---|---|---|---|
| BTC/USD | $61,113.70 | Waiting | Waiting | Waiting | In position |
| ETH/USD | $1,717.36 | Waiting | Waiting | Waiting | Waiting |

## Strategy trials

One independent paper trial per worker minute. Net P&L includes modeled costs.

| Strategy | Closed | Realized P&L | Shortlisted | Next-day validation P&L |
|---|---:|---:|---|---:|
| trend | 9 | $+0.47 | Yes | — |
| reversion | 18 | $-4.62 | Yes | $+0.35 |
| breakout | 13 | $-3.73 | Pending | — |
| momentum | 13 | $-4.55 | Yes | $+3.74 |
| relative_strength | 3 | $-4.41 | Pending | — |
| vwap_pullback | 21 | $-3.71 | Pending | — |
| failed_breakdown | 20 | $-4.14 | Yes | $+2.21 |
| grok_pullback | 15 | $-8.81 | Pending | — |
| grok_squeeze | 9 | $-5.95 | Pending | — |
| grok_supertrend | 10 | $-2.52 | Yes | $+3.75 |
| grok_stochastic | 5 | $+0.64 | Yes | — |
| grok_confluence | 7 | $+4.97 | Yes | — |

Relative strength trial equity: $195.51. 50/50 BTC–ETH buy-and-hold liquidation value: $185.52.

Validation leader: grok_supertrend

Started with $200 simulated USD. Entries and exits are modeled from candles. No broker orders.

[Refresh history](https://github.com/acerbzzz/Trade-bot-/actions/workflows/forward-paper.yml)

Last successful market check: **2026-11-23 00:33 UTC** · Target interval: 1 minute.
Worker started: **2026-11-22 23:33 UTC** · [Worker run](https://github.com/acerbzzz/Trade-bot-/actions/runs/45083889930) · [Restored checkpoint](https://github.com/acerbzzz/Trade-bot-/commit/69e37760da0dad666cb60cc501463ca6f1d699f2)

[Open phone dashboard](https://ryans-paper-desk.enchantingchili2.chatgpt.site)
