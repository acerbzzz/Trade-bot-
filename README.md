# Crypto paper desk

**Monitoring** · Kraken spot · 15-minute candles

Latest completed candle ended **2026-11-27 12:15 UTC**.

| Paper equity | Open positions | Closed trades |
|---:|---:|---:|
| $187.22 | 0 | 49 |

| Market | Last close | Trend | Mean reversion | Breakout | Momentum |
|---|---:|---|---|---|---|
| BTC/USD | $61,553.10 | Waiting | Waiting | Waiting | Waiting |
| ETH/USD | $1,719.55 | Waiting | Waiting | Waiting | Waiting |

## Strategy trials

One independent paper trial per worker minute. Net P&L includes modeled costs.

| Strategy | Closed | Realized P&L | Shortlisted | Next-day validation P&L |
|---|---:|---:|---|---:|
| trend | 12 | $-3.09 | Yes | $+0.00 |
| reversion | 25 | $-1.45 | Yes | $+1.71 |
| breakout | 19 | $-6.45 | Pending | — |
| momentum | 25 | $-10.08 | Yes | $-1.20 |
| relative_strength | 6 | $-3.72 | Pending | — |
| vwap_pullback | 44 | $-13.68 | Pending | — |
| failed_breakdown | 29 | $-8.85 | Yes | $+0.00 |
| grok_pullback | 26 | $-16.70 | Pending | — |
| grok_squeeze | 11 | $-7.90 | Pending | — |
| grok_supertrend | 15 | $+3.10 | Yes | $-1.52 |
| grok_stochastic | 11 | $-3.41 | Yes | $-0.51 |
| grok_confluence | 16 | $-0.44 | Yes | $-2.31 |

Relative strength trial equity: $196.28. 50/50 BTC–ETH buy-and-hold liquidation value: $185.99.

Validation leader: reversion

Started with $200 simulated USD. Entries and exits are modeled from candles. No broker orders.

[Refresh history](https://github.com/acerbzzz/Trade-bot-/actions/workflows/forward-paper.yml)

Last successful market check: **2026-11-27 12:28 UTC** · Target interval: 1 minute.
Worker started: **2026-11-27 11:00 UTC** · [Worker run](https://github.com/acerbzzz/Trade-bot-/actions/runs/45986828733) · [Restored checkpoint](https://github.com/acerbzzz/Trade-bot-/commit/684e55975175e2e483d4855e4a71147056f8df7e)

[Open phone dashboard](https://ryans-paper-desk.enchantingchili2.chatgpt.site)
