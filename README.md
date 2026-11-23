# Crypto paper desk

**Monitoring** · Kraken spot · 15-minute candles

Latest completed candle ended **2026-11-23 14:00 UTC**.

| Paper equity | Open positions | Closed trades |
|---:|---:|---:|
| $190.19 | 0 | 32 |

| Market | Last close | Trend | Mean reversion | Breakout | Momentum |
|---|---:|---|---|---|---|
| BTC/USD | $63,803.80 | Waiting | Waiting | Entry signal | Entry signal |
| ETH/USD | $1,810.42 | Waiting | Waiting | Entry signal | Waiting |

## Strategy trials

One independent paper trial per worker minute. Net P&L includes modeled costs.

| Strategy | Closed | Realized P&L | Shortlisted | Next-day validation P&L |
|---|---:|---:|---|---:|
| trend | 10 | $-0.10 | Yes | — |
| reversion | 18 | $-4.62 | Yes | $-2.91 |
| breakout | 14 | $-4.49 | Pending | — |
| momentum | 17 | $-6.80 | Yes | $-2.15 |
| relative_strength | 4 | $-5.87 | Pending | — |
| vwap_pullback | 26 | $-6.86 | Pending | — |
| failed_breakdown | 20 | $-4.14 | Yes | $+0.00 |
| grok_pullback | 19 | $-10.87 | Pending | — |
| grok_squeeze | 9 | $-5.95 | Pending | — |
| grok_supertrend | 11 | $+1.17 | Yes | $+3.75 |
| grok_stochastic | 7 | $-0.54 | Yes | — |
| grok_confluence | 8 | $+4.39 | Yes | $+3.74 |

Relative strength trial equity: $194.13. 50/50 BTC–ETH buy-and-hold liquidation value: $194.29.

Validation leader: grok_supertrend

Started with $200 simulated USD. Entries and exits are modeled from candles. No broker orders.

[Refresh history](https://github.com/acerbzzz/Trade-bot-/actions/workflows/forward-paper.yml)

Last successful market check: **2026-11-23 14:12 UTC** · Target interval: 1 minute.
Worker started: **2026-11-23 13:04 UTC** · [Worker run](https://github.com/acerbzzz/Trade-bot-/actions/runs/45180135830) · [Restored checkpoint](https://github.com/acerbzzz/Trade-bot-/commit/9d8eb4e2c7b453a8e85d054b7bb9c6f67fc44a76)

[Open phone dashboard](https://ryans-paper-desk.enchantingchili2.chatgpt.site)
