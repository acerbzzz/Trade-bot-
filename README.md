# Crypto paper desk

**Monitoring** · Kraken spot · 15-minute candles

Latest completed candle ended **2026-11-20 03:45 UTC**.

| Paper equity | Open positions | Closed trades |
|---:|---:|---:|
| $196.62 | 1 | 15 |

| Market | Last close | Trend | Mean reversion | Breakout | Momentum |
|---|---:|---|---|---|---|
| BTC/USD | $62,082.50 | Waiting | Waiting | Waiting | Waiting |
| ETH/USD | $1,747.97 | Waiting | In position | Waiting | Waiting |

## Strategy trials

One independent paper trial per worker minute. Net P&L includes modeled costs.

| Strategy | Closed | Realized P&L | Shortlisted | Next-day validation P&L |
|---|---:|---:|---|---:|
| trend | 6 | $-5.99 | Pending | — |
| reversion | 11 | $+0.43 | Yes | $+0.94 |
| breakout | 9 | $-6.35 | Pending | — |
| momentum | 9 | $-4.63 | Yes | $-1.07 |
| relative_strength | 2 | $-2.99 | Pending | — |
| vwap_pullback | 12 | $-6.40 | Pending | — |
| failed_breakdown | 14 | $-2.83 | Yes | $-0.56 |
| grok_pullback | 10 | $-10.46 | Pending | — |
| grok_squeeze | 5 | $-4.17 | Pending | — |
| grok_supertrend | 6 | $-6.84 | Yes | $+0.00 |
| grok_stochastic | 1 | $-0.18 | Pending | — |
| grok_confluence | 5 | $-2.50 | Pending | — |

Relative strength trial equity: $197.01. 50/50 BTC–ETH buy-and-hold liquidation value: $188.32.

Validation leader: reversion

Started with $200 simulated USD. Entries and exits are modeled from candles. No broker orders.

[Refresh history](https://github.com/acerbzzz/Trade-bot-/actions/workflows/forward-paper.yml)

Last successful market check: **2026-11-20 03:53 UTC** · Target interval: 1 minute.
Worker started: **2026-11-20 03:49 UTC** · [Worker run](https://github.com/acerbzzz/Trade-bot-/actions/runs/44670296774) · [Restored checkpoint](https://github.com/acerbzzz/Trade-bot-/commit/e789ee930482515ac3864d4da5b0869918b4b798)

[Open phone dashboard](https://ryans-paper-desk.enchantingchili2.chatgpt.site)
