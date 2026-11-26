# Crypto paper desk

**Monitoring** · Kraken spot · 15-minute candles

Latest completed candle ended **2026-11-26 13:00 UTC**.

| Paper equity | Open positions | Closed trades |
|---:|---:|---:|
| $184.07 | 1 | 44 |

| Market | Last close | Trend | Mean reversion | Breakout | Momentum |
|---|---:|---|---|---|---|
| BTC/USD | $60,762.90 | Waiting | Waiting | Waiting | In position |
| ETH/USD | $1,704.67 | Waiting | Waiting | Waiting | Waiting |

## Strategy trials

One independent paper trial per worker minute. Net P&L includes modeled costs.

| Strategy | Closed | Realized P&L | Shortlisted | Next-day validation P&L |
|---|---:|---:|---|---:|
| trend | 12 | $-3.09 | Yes | $+0.00 |
| reversion | 24 | $-3.13 | Yes | $+1.05 |
| breakout | 17 | $-5.72 | Pending | — |
| momentum | 23 | $-12.75 | Yes | $-1.36 |
| relative_strength | 5 | $-7.33 | Pending | — |
| vwap_pullback | 38 | $-13.33 | Pending | — |
| failed_breakdown | 29 | $-8.85 | Yes | $+0.79 |
| grok_pullback | 23 | $-13.85 | Pending | — |
| grok_squeeze | 11 | $-7.90 | Pending | — |
| grok_supertrend | 12 | $-0.33 | Yes | $+2.11 |
| grok_stochastic | 9 | $-1.68 | Yes | $+0.00 |
| grok_confluence | 13 | $+1.39 | Yes | $+1.64 |

Relative strength trial equity: $193.45. 50/50 BTC–ETH buy-and-hold liquidation value: $183.99.

Validation leader: grok_supertrend

Started with $200 simulated USD. Entries and exits are modeled from candles. No broker orders.

[Refresh history](https://github.com/acerbzzz/Trade-bot-/actions/workflows/forward-paper.yml)

Last successful market check: **2026-11-26 13:05 UTC** · Target interval: 1 minute.
Worker started: **2026-11-26 12:30 UTC** · [Worker run](https://github.com/acerbzzz/Trade-bot-/actions/runs/45810858047) · [Restored checkpoint](https://github.com/acerbzzz/Trade-bot-/commit/ba7fab750872b0fb96808ecf19a11cd13e403bac)

[Open phone dashboard](https://ryans-paper-desk.enchantingchili2.chatgpt.site)
