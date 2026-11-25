# Crypto paper desk

**Monitoring** · Kraken spot · 15-minute candles

Latest completed candle ended **2026-11-25 04:30 UTC**.

| Paper equity | Open positions | Closed trades |
|---:|---:|---:|
| $186.70 | 1 | 37 |

| Market | Last close | Trend | Mean reversion | Breakout | Momentum |
|---|---:|---|---|---|---|
| BTC/USD | $59,200.90 | Waiting | Waiting | Waiting | Waiting |
| ETH/USD | $1,660.79 | Waiting | In position | Waiting | Waiting |

## Strategy trials

One independent paper trial per worker minute. Net P&L includes modeled costs.

| Strategy | Closed | Realized P&L | Shortlisted | Next-day validation P&L |
|---|---:|---:|---|---:|
| trend | 12 | $-3.09 | Yes | $-2.99 |
| reversion | 20 | $-4.16 | Yes | $+0.46 |
| breakout | 16 | $-7.40 | Pending | — |
| momentum | 19 | $-9.68 | Yes | $-1.50 |
| relative_strength | 5 | $-7.33 | Pending | — |
| vwap_pullback | 31 | $-10.53 | Pending | — |
| failed_breakdown | 25 | $-10.05 | Yes | $-4.65 |
| grok_pullback | 21 | $-12.92 | Pending | — |
| grok_squeeze | 10 | $-7.41 | Pending | — |
| grok_supertrend | 12 | $-0.33 | Yes | $-1.50 |
| grok_stochastic | 8 | $-1.17 | Yes | $+0.00 |
| grok_confluence | 11 | $+0.17 | Yes | $-2.66 |

Relative strength trial equity: $192.67. 50/50 BTC–ETH buy-and-hold liquidation value: $179.28.

Validation leader: reversion

Started with $200 simulated USD. Entries and exits are modeled from candles. No broker orders.

[Refresh history](https://github.com/acerbzzz/Trade-bot-/actions/workflows/forward-paper.yml)

Last successful market check: **2026-11-25 04:34 UTC** · Target interval: 1 minute.
Worker started: **2026-11-25 03:08 UTC** · [Worker run](https://github.com/acerbzzz/Trade-bot-/actions/runs/45537868342) · [Restored checkpoint](https://github.com/acerbzzz/Trade-bot-/commit/ae9742fa4a8c02cb9af5b59670ac4ee9cdb88515)

[Open phone dashboard](https://ryans-paper-desk.enchantingchili2.chatgpt.site)
