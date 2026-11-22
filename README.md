# Crypto paper desk

**Monitoring** · Kraken spot · 15-minute candles

Latest completed candle ended **2026-11-22 13:15 UTC**.

| Paper equity | Open positions | Closed trades |
|---:|---:|---:|
| $193.70 | 1 | 27 |

| Market | Last close | Trend | Mean reversion | Breakout | Momentum |
|---|---:|---|---|---|---|
| BTC/USD | $60,697.70 | Waiting | Waiting | In position | Waiting |
| ETH/USD | $1,703.00 | Waiting | Waiting | Waiting | Waiting |

## Strategy trials

One independent paper trial per worker minute. Net P&L includes modeled costs.

| Strategy | Closed | Realized P&L | Shortlisted | Next-day validation P&L |
|---|---:|---:|---|---:|
| trend | 9 | $+0.47 | Yes | — |
| reversion | 18 | $-4.62 | Yes | $+0.35 |
| breakout | 12 | $-2.66 | Pending | — |
| momentum | 11 | $-2.47 | Yes | $+3.74 |
| relative_strength | 3 | $-4.41 | Pending | — |
| vwap_pullback | 21 | $-3.71 | Pending | — |
| failed_breakdown | 20 | $-4.14 | Yes | $+2.21 |
| grok_pullback | 13 | $-7.73 | Pending | — |
| grok_squeeze | 7 | $-3.83 | Pending | — |
| grok_supertrend | 10 | $-2.52 | Yes | $+3.75 |
| grok_stochastic | 2 | $-0.32 | Pending | — |
| grok_confluence | 7 | $+4.97 | Yes | — |

Relative strength trial equity: $195.59. 50/50 BTC–ETH buy-and-hold liquidation value: $183.80.

Validation leader: grok_supertrend

Started with $200 simulated USD. Entries and exits are modeled from candles. No broker orders.

[Refresh history](https://github.com/acerbzzz/Trade-bot-/actions/workflows/forward-paper.yml)

Last successful market check: **2026-11-22 13:29 UTC** · Target interval: 1 minute.
Worker started: **2026-11-22 12:49 UTC** · [Worker run](https://github.com/acerbzzz/Trade-bot-/actions/runs/45024264384) · [Restored checkpoint](https://github.com/acerbzzz/Trade-bot-/commit/c8a120cbc2213820c15e71b0233ee00613b1c154)

[Open phone dashboard](https://ryans-paper-desk.enchantingchili2.chatgpt.site)
