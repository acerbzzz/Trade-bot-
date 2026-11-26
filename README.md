# Crypto paper desk

**Monitoring** · Kraken spot · 15-minute candles

Latest completed candle ended **2026-11-26 23:45 UTC**.

| Paper equity | Open positions | Closed trades |
|---:|---:|---:|
| $184.07 | 0 | 47 |

| Market | Last close | Trend | Mean reversion | Breakout | Momentum |
|---|---:|---|---|---|---|
| BTC/USD | $60,417.80 | Waiting | Waiting | Waiting | Waiting |
| ETH/USD | $1,685.02 | Waiting | Waiting | Waiting | Waiting |

## Strategy trials

One independent paper trial per worker minute. Net P&L includes modeled costs.

| Strategy | Closed | Realized P&L | Shortlisted | Next-day validation P&L |
|---|---:|---:|---|---:|
| trend | 12 | $-3.09 | Yes | $+0.00 |
| reversion | 25 | $-1.45 | Yes | $+1.05 |
| breakout | 18 | $-6.94 | Pending | — |
| momentum | 24 | $-13.57 | Yes | $-1.36 |
| relative_strength | 5 | $-7.33 | Pending | — |
| vwap_pullback | 40 | $-14.77 | Pending | — |
| failed_breakdown | 29 | $-8.85 | Yes | $+0.79 |
| grok_pullback | 24 | $-14.99 | Pending | — |
| grok_squeeze | 11 | $-7.90 | Pending | — |
| grok_supertrend | 14 | $-0.64 | Yes | $+2.11 |
| grok_stochastic | 9 | $-1.68 | Yes | $+0.00 |
| grok_confluence | 15 | $-0.94 | Yes | $+1.64 |

Relative strength trial equity: $192.67. 50/50 BTC–ETH buy-and-hold liquidation value: $182.40.

Validation leader: grok_supertrend

Started with $200 simulated USD. Entries and exits are modeled from candles. No broker orders.

[Refresh history](https://github.com/acerbzzz/Trade-bot-/actions/workflows/forward-paper.yml)

Last successful market check: **2026-11-26 23:52 UTC** · Target interval: 1 minute.
Worker started: **2026-11-26 23:00 UTC** · [Worker run](https://github.com/acerbzzz/Trade-bot-/actions/runs/45908278040) · [Restored checkpoint](https://github.com/acerbzzz/Trade-bot-/commit/32dff94d6dc91e1758544b6bca75fcd0b0dbf001)

[Open phone dashboard](https://ryans-paper-desk.enchantingchili2.chatgpt.site)
