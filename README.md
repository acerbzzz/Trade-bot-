# Crypto paper desk

**Monitoring** · Kraken spot · 15-minute candles

Latest completed candle ended **2026-11-26 08:00 UTC**.

| Paper equity | Open positions | Closed trades |
|---:|---:|---:|
| $185.34 | 0 | 43 |

| Market | Last close | Trend | Mean reversion | Breakout | Momentum |
|---|---:|---|---|---|---|
| BTC/USD | $60,454.90 | Waiting | Waiting | Waiting | Waiting |
| ETH/USD | $1,687.84 | Waiting | Waiting | Waiting | Waiting |

## Strategy trials

One independent paper trial per worker minute. Net P&L includes modeled costs.

| Strategy | Closed | Realized P&L | Shortlisted | Next-day validation P&L |
|---|---:|---:|---|---:|
| trend | 12 | $-3.09 | Yes | $+0.00 |
| reversion | 24 | $-3.13 | Yes | $+1.05 |
| breakout | 17 | $-5.72 | Pending | — |
| momentum | 22 | $-11.87 | Yes | $-1.36 |
| relative_strength | 5 | $-7.33 | Pending | — |
| vwap_pullback | 36 | $-11.20 | Pending | — |
| failed_breakdown | 29 | $-8.85 | Yes | $+0.79 |
| grok_pullback | 22 | $-12.45 | Pending | — |
| grok_squeeze | 11 | $-7.90 | Pending | — |
| grok_supertrend | 12 | $-0.33 | Yes | $+2.11 |
| grok_stochastic | 9 | $-1.68 | Yes | $+0.00 |
| grok_confluence | 13 | $+1.39 | Yes | $+1.64 |

Relative strength trial equity: $192.76. 50/50 BTC–ETH buy-and-hold liquidation value: $182.61.

Validation leader: grok_supertrend

Started with $200 simulated USD. Entries and exits are modeled from candles. No broker orders.

[Refresh history](https://github.com/acerbzzz/Trade-bot-/actions/workflows/forward-paper.yml)

Last successful market check: **2026-11-26 08:10 UTC** · Target interval: 1 minute.
Worker started: **2026-11-26 08:00 UTC** · [Worker run](https://github.com/acerbzzz/Trade-bot-/actions/runs/45779562679) · [Restored checkpoint](https://github.com/acerbzzz/Trade-bot-/commit/f73fc12c74ecba399f733ecbce41e557f1e444ca)

[Open phone dashboard](https://ryans-paper-desk.enchantingchili2.chatgpt.site)
