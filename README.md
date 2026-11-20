# Crypto paper desk

**Monitoring** · Kraken spot · 15-minute candles

Latest completed candle ended **2026-11-20 16:00 UTC**.

| Paper equity | Open positions | Closed trades |
|---:|---:|---:|
| $191.71 | 0 | 19 |

| Market | Last close | Trend | Mean reversion | Breakout | Momentum |
|---|---:|---|---|---|---|
| BTC/USD | $59,399.90 | Waiting | Entry signal | Waiting | Waiting |
| ETH/USD | $1,653.53 | Waiting | Entry signal | Waiting | Waiting |

## Strategy trials

One independent paper trial per worker minute. Net P&L includes modeled costs.

| Strategy | Closed | Realized P&L | Shortlisted | Next-day validation P&L |
|---|---:|---:|---|---:|
| trend | 6 | $-5.99 | Pending | — |
| reversion | 12 | $+0.93 | Yes | $+0.94 |
| breakout | 10 | $-7.80 | Pending | — |
| momentum | 10 | $-6.10 | Yes | $-1.07 |
| relative_strength | 2 | $-2.99 | Pending | — |
| vwap_pullback | 16 | $-9.87 | Pending | — |
| failed_breakdown | 15 | $-3.46 | Yes | $-0.56 |
| grok_pullback | 10 | $-10.46 | Pending | — |
| grok_squeeze | 6 | $-5.64 | Pending | — |
| grok_supertrend | 7 | $-8.28 | Yes | $+0.00 |
| grok_stochastic | 1 | $-0.18 | Pending | — |
| grok_confluence | 5 | $-2.50 | Pending | — |

Relative strength trial equity: $197.01. 50/50 BTC–ETH buy-and-hold liquidation value: $179.16.

Validation leader: reversion

Started with $200 simulated USD. Entries and exits are modeled from candles. No broker orders.

[Refresh history](https://github.com/acerbzzz/Trade-bot-/actions/workflows/forward-paper.yml)

Last successful market check: **2026-11-20 16:02 UTC** · Target interval: 1 minute.
Worker started: **2026-11-20 15:49 UTC** · [Worker run](https://github.com/acerbzzz/Trade-bot-/actions/runs/44767132273) · [Restored checkpoint](https://github.com/acerbzzz/Trade-bot-/commit/8b5b2fab224a669bb6929b7e57cf083f1066bea4)

[Open phone dashboard](https://ryans-paper-desk.enchantingchili2.chatgpt.site)
