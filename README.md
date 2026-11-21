# Crypto paper desk

**Monitoring** · Kraken spot · 15-minute candles

Latest completed candle ended **2026-11-21 18:45 UTC**.

| Paper equity | Open positions | Closed trades |
|---:|---:|---:|
| $193.73 | 1 | 23 |

| Market | Last close | Trend | Mean reversion | Breakout | Momentum |
|---|---:|---|---|---|---|
| BTC/USD | $60,061.90 | Waiting | Waiting | In position | Waiting |
| ETH/USD | $1,680.91 | Waiting | Waiting | Waiting | Waiting |

## Strategy trials

One independent paper trial per worker minute. Net P&L includes modeled costs.

| Strategy | Closed | Realized P&L | Shortlisted | Next-day validation P&L |
|---|---:|---:|---|---:|
| trend | 6 | $-5.99 | Pending | — |
| reversion | 16 | $-1.73 | Yes | $-2.49 |
| breakout | 11 | $-6.28 | Pending | — |
| momentum | 11 | $-2.47 | Yes | $-1.50 |
| relative_strength | 2 | $-2.99 | Pending | — |
| vwap_pullback | 20 | $-7.32 | Pending | — |
| failed_breakdown | 20 | $-4.14 | Yes | $-1.59 |
| grok_pullback | 11 | $-6.90 | Pending | — |
| grok_squeeze | 7 | $-3.83 | Pending | — |
| grok_supertrend | 9 | $-6.16 | Yes | $-2.12 |
| grok_stochastic | 1 | $-0.18 | Pending | — |
| grok_confluence | 6 | $+1.20 | Yes | — |

Relative strength trial equity: $197.01. 50/50 BTC–ETH buy-and-hold liquidation value: $181.79.

Validation leader: None profitable

Started with $200 simulated USD. Entries and exits are modeled from candles. No broker orders.

[Refresh history](https://github.com/acerbzzz/Trade-bot-/actions/workflows/forward-paper.yml)

Last successful market check: **2026-11-21 18:46 UTC** · Target interval: 1 minute.
Worker started: **2026-11-21 17:19 UTC** · [Worker run](https://github.com/acerbzzz/Trade-bot-/actions/runs/44927237012) · [Restored checkpoint](https://github.com/acerbzzz/Trade-bot-/commit/1c6a81dadd347ca822dcf71b1e65de8ebaa7351c)

[Open phone dashboard](https://ryans-paper-desk.enchantingchili2.chatgpt.site)
