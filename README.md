# Crypto paper desk

**Monitoring** · Kraken spot · 15-minute candles

Latest completed candle ended **2026-11-22 19:45 UTC**.

| Paper equity | Open positions | Closed trades |
|---:|---:|---:|
| $192.73 | 0 | 29 |

| Market | Last close | Trend | Mean reversion | Breakout | Momentum |
|---|---:|---|---|---|---|
| BTC/USD | $60,646.50 | Waiting | Waiting | Waiting | Waiting |
| ETH/USD | $1,712.61 | Waiting | Waiting | Waiting | Waiting |

## Strategy trials

One independent paper trial per worker minute. Net P&L includes modeled costs.

| Strategy | Closed | Realized P&L | Shortlisted | Next-day validation P&L |
|---|---:|---:|---|---:|
| trend | 9 | $+0.47 | Yes | — |
| reversion | 18 | $-4.62 | Yes | $+0.35 |
| breakout | 13 | $-3.73 | Pending | — |
| momentum | 12 | $-3.09 | Yes | $+3.74 |
| relative_strength | 3 | $-4.41 | Pending | — |
| vwap_pullback | 21 | $-3.71 | Pending | — |
| failed_breakdown | 20 | $-4.14 | Yes | $+2.21 |
| grok_pullback | 14 | $-8.03 | Pending | — |
| grok_squeeze | 8 | $-4.50 | Pending | — |
| grok_supertrend | 10 | $-2.52 | Yes | $+3.75 |
| grok_stochastic | 4 | $-0.19 | Yes | — |
| grok_confluence | 7 | $+4.97 | Yes | — |

Relative strength trial equity: $195.59. 50/50 BTC–ETH buy-and-hold liquidation value: $184.31.

Validation leader: grok_supertrend

Started with $200 simulated USD. Entries and exits are modeled from candles. No broker orders.

[Refresh history](https://github.com/acerbzzz/Trade-bot-/actions/workflows/forward-paper.yml)

Last successful market check: **2026-11-22 19:46 UTC** · Target interval: 1 minute.
Worker started: **2026-11-22 18:49 UTC** · [Worker run](https://github.com/acerbzzz/Trade-bot-/actions/runs/45057246953) · [Restored checkpoint](https://github.com/acerbzzz/Trade-bot-/commit/6b2df51b9dfda8427545c5b3a7177b7b22a95fa4)

[Open phone dashboard](https://ryans-paper-desk.enchantingchili2.chatgpt.site)
