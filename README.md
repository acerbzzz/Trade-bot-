# Crypto paper desk

**Monitoring** · Kraken spot · 15-minute candles

Latest completed candle ended **2026-11-26 04:15 UTC**.

| Paper equity | Open positions | Closed trades |
|---:|---:|---:|
| $185.34 | 0 | 43 |

| Market | Last close | Trend | Mean reversion | Breakout | Momentum |
|---|---:|---|---|---|---|
| BTC/USD | $60,917.80 | Waiting | Waiting | Waiting | Waiting |
| ETH/USD | $1,701.39 | Waiting | Waiting | Waiting | Waiting |

## Strategy trials

One independent paper trial per worker minute. Net P&L includes modeled costs.

| Strategy | Closed | Realized P&L | Shortlisted | Next-day validation P&L |
|---|---:|---:|---|---:|
| trend | 12 | $-3.09 | Yes | $+0.00 |
| reversion | 24 | $-3.13 | Yes | $+1.05 |
| breakout | 17 | $-5.72 | Pending | — |
| momentum | 22 | $-11.87 | Yes | $-1.36 |
| relative_strength | 5 | $-7.33 | Pending | — |
| vwap_pullback | 35 | $-10.54 | Pending | — |
| failed_breakdown | 29 | $-8.85 | Yes | $+0.79 |
| grok_pullback | 21 | $-12.92 | Pending | — |
| grok_squeeze | 10 | $-7.41 | Pending | — |
| grok_supertrend | 12 | $-0.33 | Yes | $+2.11 |
| grok_stochastic | 8 | $-1.17 | Yes | $+0.00 |
| grok_confluence | 13 | $+1.39 | Yes | $+1.64 |

Relative strength trial equity: $193.29. 50/50 BTC–ETH buy-and-hold liquidation value: $183.40.

Validation leader: grok_supertrend

Started with $200 simulated USD. Entries and exits are modeled from candles. No broker orders.

[Refresh history](https://github.com/acerbzzz/Trade-bot-/actions/workflows/forward-paper.yml)

Last successful market check: **2026-11-26 04:19 UTC** · Target interval: 1 minute.
Worker started: **2026-11-26 03:30 UTC** · [Worker run](https://github.com/acerbzzz/Trade-bot-/actions/runs/45744047877) · [Restored checkpoint](https://github.com/acerbzzz/Trade-bot-/commit/6786335f41db3cc4741b41de202ef2bc889af644)

[Open phone dashboard](https://ryans-paper-desk.enchantingchili2.chatgpt.site)
