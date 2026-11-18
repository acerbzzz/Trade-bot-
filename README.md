# Crypto paper desk

**Monitoring** · Kraken spot · 15-minute candles

Latest completed candle ended **2026-11-18 05:45 UTC**.

| Paper equity | Open positions | Closed trades |
|---:|---:|---:|
| $196.72 | 1 | 7 |

| Market | Last close | Trend | Mean reversion | Breakout | Momentum |
|---|---:|---|---|---|---|
| BTC/USD | $64,632.80 | Waiting | Waiting | Waiting | In position |
| ETH/USD | $1,811.21 | Waiting | Waiting | Waiting | Waiting |

## Strategy trials

One independent paper trial per worker minute. Net P&L includes modeled costs.

| Strategy | Closed | Realized P&L | Shortlisted | Next-day validation P&L |
|---|---:|---:|---|---:|
| trend | 4 | $-4.73 | Pending | — |
| reversion | 6 | $+0.15 | Yes | — |
| breakout | 7 | $-5.47 | Pending | — |
| momentum | 6 | $-3.26 | Yes | $-1.70 |
| relative_strength | 2 | $-2.99 | Pending | — |
| vwap_pullback | 10 | $-5.19 | Pending | — |
| failed_breakdown | 10 | $+0.56 | Yes | $-1.57 |
| grok_pullback | 7 | $-8.90 | Pending | — |
| grok_squeeze | 4 | $-2.77 | Pending | — |
| grok_supertrend | 4 | $-4.06 | Yes | $-2.89 |
| grok_stochastic | 1 | $-0.18 | Pending | — |
| grok_confluence | 4 | $-2.72 | Pending | — |

Relative strength trial equity: $197.01. 50/50 BTC–ETH buy-and-hold liquidation value: $195.59.

Validation leader: None profitable

Started with $200 simulated USD. Entries and exits are modeled from candles. No broker orders.

[Refresh history](https://github.com/acerbzzz/Trade-bot-/actions/workflows/forward-paper.yml)

Last successful market check: **2026-11-18 05:58 UTC** · Target interval: 1 minute.
Worker started: **2026-11-18 05:19 UTC** · [Worker run](https://github.com/acerbzzz/Trade-bot-/actions/runs/44243444232) · [Restored checkpoint](https://github.com/acerbzzz/Trade-bot-/commit/f442345bd5b8d47f55ca7510cd965b3e4ed5b5a6)

[Open phone dashboard](https://ryans-paper-desk.enchantingchili2.chatgpt.site)
