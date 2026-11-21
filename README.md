# Crypto paper desk

**Monitoring** · Kraken spot · 15-minute candles

Latest completed candle ended **2026-11-21 04:15 UTC**.

| Paper equity | Open positions | Closed trades |
|---:|---:|---:|
| $188.86 | 0 | 21 |

| Market | Last close | Trend | Mean reversion | Breakout | Momentum |
|---|---:|---|---|---|---|
| BTC/USD | $55,831.00 | Waiting | Entry signal | Waiting | Waiting |
| ETH/USD | $1,551.99 | Waiting | Entry signal | Waiting | Waiting |

## Strategy trials

One independent paper trial per worker minute. Net P&L includes modeled costs.

| Strategy | Closed | Realized P&L | Shortlisted | Next-day validation P&L |
|---|---:|---:|---|---:|
| trend | 6 | $-5.99 | Pending | — |
| reversion | 14 | $-2.06 | Yes | $-2.49 |
| breakout | 10 | $-7.80 | Pending | — |
| momentum | 10 | $-6.10 | Yes | $-1.50 |
| relative_strength | 2 | $-2.99 | Pending | — |
| vwap_pullback | 19 | $-10.86 | Pending | — |
| failed_breakdown | 19 | $-7.73 | Yes | $-1.59 |
| grok_pullback | 10 | $-10.46 | Pending | — |
| grok_squeeze | 6 | $-5.64 | Pending | — |
| grok_supertrend | 8 | $-9.71 | Yes | $-2.12 |
| grok_stochastic | 1 | $-0.18 | Pending | — |
| grok_confluence | 5 | $-2.50 | Pending | — |

Relative strength trial equity: $197.01. 50/50 BTC–ETH buy-and-hold liquidation value: $170.41.

Validation leader: None profitable

Started with $200 simulated USD. Entries and exits are modeled from candles. No broker orders.

[Refresh history](https://github.com/acerbzzz/Trade-bot-/actions/workflows/forward-paper.yml)

Last successful market check: **2026-11-21 04:16 UTC** · Target interval: 1 minute.
Worker started: **2026-11-21 03:49 UTC** · [Worker run](https://github.com/acerbzzz/Trade-bot-/actions/runs/44863057629) · [Restored checkpoint](https://github.com/acerbzzz/Trade-bot-/commit/1182cc027dfc01596340fd23699a539c09b0b77a)

[Open phone dashboard](https://ryans-paper-desk.enchantingchili2.chatgpt.site)
