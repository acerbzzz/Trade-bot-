# Crypto paper desk

**Monitoring** · Kraken spot · 15-minute candles

Latest completed candle ended **2026-11-23 11:15 UTC**.

| Paper equity | Open positions | Closed trades |
|---:|---:|---:|
| $190.39 | 1 | 31 |

| Market | Last close | Trend | Mean reversion | Breakout | Momentum |
|---|---:|---|---|---|---|
| BTC/USD | $61,228.60 | In position | Waiting | Waiting | Waiting |
| ETH/USD | $1,720.46 | Waiting | Waiting | Waiting | Waiting |

## Strategy trials

One independent paper trial per worker minute. Net P&L includes modeled costs.

| Strategy | Closed | Realized P&L | Shortlisted | Next-day validation P&L |
|---|---:|---:|---|---:|
| trend | 9 | $+0.47 | Yes | — |
| reversion | 18 | $-4.62 | Yes | $-2.91 |
| breakout | 14 | $-4.49 | Pending | — |
| momentum | 16 | $-5.93 | Yes | $-2.15 |
| relative_strength | 4 | $-5.87 | Pending | — |
| vwap_pullback | 23 | $-5.07 | Pending | — |
| failed_breakdown | 20 | $-4.14 | Yes | $+0.00 |
| grok_pullback | 19 | $-10.87 | Pending | — |
| grok_squeeze | 9 | $-5.95 | Pending | — |
| grok_supertrend | 10 | $-2.52 | Yes | $+3.75 |
| grok_stochastic | 5 | $+0.64 | Yes | — |
| grok_confluence | 8 | $+4.39 | Yes | $+3.74 |

Relative strength trial equity: $194.13. 50/50 BTC–ETH buy-and-hold liquidation value: $185.87.

Validation leader: grok_supertrend

Started with $200 simulated USD. Entries and exits are modeled from candles. No broker orders.

[Refresh history](https://github.com/acerbzzz/Trade-bot-/actions/workflows/forward-paper.yml)

Last successful market check: **2026-11-23 11:15 UTC** · Target interval: 1 minute.
Worker started: **2026-11-23 10:03 UTC** · [Worker run](https://github.com/acerbzzz/Trade-bot-/actions/runs/45152573604) · [Restored checkpoint](https://github.com/acerbzzz/Trade-bot-/commit/97fb83a4b5a13db77bf151e94b5b71d85c964621)

[Open phone dashboard](https://ryans-paper-desk.enchantingchili2.chatgpt.site)
