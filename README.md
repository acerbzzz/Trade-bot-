# Crypto paper desk

**Monitoring** · Kraken spot · 15-minute candles

Latest completed candle ended **2026-11-18 01:30 UTC**.

| Paper equity | Open positions | Closed trades |
|---:|---:|---:|
| $197.34 | 1 | 6 |

| Market | Last close | Trend | Mean reversion | Breakout | Momentum |
|---|---:|---|---|---|---|
| BTC/USD | $64,516.20 | Waiting | Waiting | In position | Waiting |
| ETH/USD | $1,809.85 | Waiting | Waiting | Waiting | Waiting |

## Strategy trials

One independent paper trial per worker minute. Net P&L includes modeled costs.

| Strategy | Closed | Realized P&L | Shortlisted | Next-day validation P&L |
|---|---:|---:|---|---:|
| trend | 4 | $-4.73 | Pending | — |
| reversion | 6 | $+0.15 | Yes | — |
| breakout | 6 | $-5.28 | Pending | — |
| momentum | 6 | $-3.26 | Yes | $-1.70 |
| relative_strength | 1 | $-1.50 | Pending | — |
| vwap_pullback | 7 | $-3.41 | Pending | — |
| failed_breakdown | 10 | $+0.56 | Yes | $-1.57 |
| grok_pullback | 6 | $-7.90 | Pending | — |
| grok_squeeze | 3 | $-2.89 | Pending | — |
| grok_supertrend | 4 | $-4.06 | Yes | $-2.89 |
| grok_stochastic | 1 | $-0.18 | Pending | — |
| grok_confluence | 4 | $-2.72 | Pending | — |

Relative strength trial equity: $197.54. 50/50 BTC–ETH buy-and-hold liquidation value: $195.34.

Validation leader: None profitable

Started with $200 simulated USD. Entries and exits are modeled from candles. No broker orders.

[Refresh history](https://github.com/acerbzzz/Trade-bot-/actions/workflows/forward-paper.yml)

Last successful market check: **2026-11-18 01:43 UTC** · Target interval: 1 minute.
Worker started: **2026-11-18 00:49 UTC** · [Worker run](https://github.com/acerbzzz/Trade-bot-/actions/runs/44210954167) · [Restored checkpoint](https://github.com/acerbzzz/Trade-bot-/commit/87d51398148f68341d6e581b55e378838685a6c8)

[Open phone dashboard](https://ryans-paper-desk.enchantingchili2.chatgpt.site)
