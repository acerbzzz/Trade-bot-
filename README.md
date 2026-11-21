# Crypto paper desk

**Monitoring** · Kraken spot · 15-minute candles

Latest completed candle ended **2026-11-21 01:00 UTC**.

| Paper equity | Open positions | Closed trades |
|---:|---:|---:|
| $190.28 | 0 | 20 |

| Market | Last close | Trend | Mean reversion | Breakout | Momentum |
|---|---:|---|---|---|---|
| BTC/USD | $58,900.30 | Waiting | Waiting | Waiting | Waiting |
| ETH/USD | $1,619.82 | Waiting | Waiting | Waiting | Waiting |

## Strategy trials

One independent paper trial per worker minute. Net P&L includes modeled costs.

| Strategy | Closed | Realized P&L | Shortlisted | Next-day validation P&L |
|---|---:|---:|---|---:|
| trend | 6 | $-5.99 | Pending | — |
| reversion | 14 | $-2.06 | Yes | $-2.49 |
| breakout | 10 | $-7.80 | Pending | — |
| momentum | 10 | $-6.10 | Yes | $-1.50 |
| relative_strength | 2 | $-2.99 | Pending | — |
| vwap_pullback | 16 | $-9.87 | Pending | — |
| failed_breakdown | 17 | $-4.82 | Yes | $-1.59 |
| grok_pullback | 10 | $-10.46 | Pending | — |
| grok_squeeze | 6 | $-5.64 | Pending | — |
| grok_supertrend | 7 | $-8.28 | Yes | $-2.12 |
| grok_stochastic | 1 | $-0.18 | Pending | — |
| grok_confluence | 5 | $-2.50 | Pending | — |

Relative strength trial equity: $197.01. 50/50 BTC–ETH buy-and-hold liquidation value: $176.59.

Validation leader: None profitable

Started with $200 simulated USD. Entries and exits are modeled from candles. No broker orders.

[Refresh history](https://github.com/acerbzzz/Trade-bot-/actions/workflows/forward-paper.yml)

Last successful market check: **2026-11-21 01:11 UTC** · Target interval: 1 minute.
Worker started: **2026-11-21 00:49 UTC** · [Worker run](https://github.com/acerbzzz/Trade-bot-/actions/runs/44846346686) · [Restored checkpoint](https://github.com/acerbzzz/Trade-bot-/commit/938bcfb11ee7fe4d09a4d182feb21769adbebb17)

[Open phone dashboard](https://ryans-paper-desk.enchantingchili2.chatgpt.site)
