# Crypto paper desk

**Monitoring** · Kraken spot · 15-minute candles

Latest completed candle ended **2026-11-17 13:00 UTC**.

| Paper equity | Open positions | Closed trades |
|---:|---:|---:|
| $198.49 | 1 | 5 |

| Market | Last close | Trend | Mean reversion | Breakout | Momentum |
|---|---:|---|---|---|---|
| BTC/USD | $64,995.40 | Waiting | Waiting | In position | Waiting |
| ETH/USD | $1,821.91 | Waiting | Waiting | Waiting | Waiting |

## Strategy trials

One independent paper trial per worker minute. Net P&L includes modeled costs.

| Strategy | Closed | Realized P&L | Shortlisted | Next-day validation P&L |
|---|---:|---:|---|---:|
| trend | 3 | $-3.26 | Pending | — |
| reversion | 6 | $+0.15 | Yes | — |
| breakout | 5 | $-4.28 | Pending | — |
| momentum | 6 | $-3.26 | Yes | $-1.70 |
| relative_strength | 1 | $-1.50 | Pending | — |
| vwap_pullback | 4 | $-3.17 | Pending | — |
| failed_breakdown | 8 | $+2.15 | Yes | — |
| grok_pullback | 5 | $-6.45 | Pending | — |
| grok_squeeze | 3 | $-2.89 | Pending | — |
| grok_supertrend | 3 | $-2.58 | Yes | $-1.13 |
| grok_stochastic | 1 | $-0.18 | Pending | — |
| grok_confluence | 3 | $-1.71 | Pending | — |

Relative strength trial equity: $198.50. 50/50 BTC–ETH buy-and-hold liquidation value: $196.72.

Validation leader: None profitable

Started with $200 simulated USD. Entries and exits are modeled from candles. No broker orders.

[Refresh history](https://github.com/acerbzzz/Trade-bot-/actions/workflows/forward-paper.yml)

Last successful market check: **2026-11-17 13:12 UTC** · Target interval: 1 minute.
Worker started: **2026-11-17 12:49 UTC** · [Worker run](https://github.com/acerbzzz/Trade-bot-/actions/runs/44084264177) · [Restored checkpoint](https://github.com/acerbzzz/Trade-bot-/commit/92a8789796f408b1e973c573c94813bb11e40ace)

[Open phone dashboard](https://ryans-paper-desk.enchantingchili2.chatgpt.site)
