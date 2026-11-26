# Crypto paper desk

**Monitoring** · Kraken spot · 15-minute candles

Latest completed candle ended **2026-11-26 03:00 UTC**.

| Paper equity | Open positions | Closed trades |
|---:|---:|---:|
| $185.44 | 1 | 42 |

| Market | Last close | Trend | Mean reversion | Breakout | Momentum |
|---|---:|---|---|---|---|
| BTC/USD | $60,631.30 | Waiting | Waiting | Waiting | In position |
| ETH/USD | $1,696.36 | Waiting | Waiting | Waiting | Waiting |

## Strategy trials

One independent paper trial per worker minute. Net P&L includes modeled costs.

| Strategy | Closed | Realized P&L | Shortlisted | Next-day validation P&L |
|---|---:|---:|---|---:|
| trend | 12 | $-3.09 | Yes | $+0.00 |
| reversion | 24 | $-3.13 | Yes | $+1.05 |
| breakout | 17 | $-5.72 | Pending | — |
| momentum | 21 | $-10.98 | Yes | $-1.36 |
| relative_strength | 5 | $-7.33 | Pending | — |
| vwap_pullback | 34 | $-9.80 | Pending | — |
| failed_breakdown | 29 | $-8.85 | Yes | $+0.79 |
| grok_pullback | 21 | $-12.92 | Pending | — |
| grok_squeeze | 10 | $-7.41 | Pending | — |
| grok_supertrend | 12 | $-0.33 | Yes | $+2.11 |
| grok_stochastic | 8 | $-1.17 | Yes | $+0.00 |
| grok_confluence | 12 | $+1.74 | Yes | $+1.64 |

Relative strength trial equity: $193.15. 50/50 BTC–ETH buy-and-hold liquidation value: $183.34.

Validation leader: grok_supertrend

Started with $200 simulated USD. Entries and exits are modeled from candles. No broker orders.

[Refresh history](https://github.com/acerbzzz/Trade-bot-/actions/workflows/forward-paper.yml)

Last successful market check: **2026-11-26 03:03 UTC** · Target interval: 1 minute.
Worker started: **2026-11-26 02:00 UTC** · [Worker run](https://github.com/acerbzzz/Trade-bot-/actions/runs/45739502238) · [Restored checkpoint](https://github.com/acerbzzz/Trade-bot-/commit/56b7f970834e934c14e387effc7d8f173934f0a1)

[Open phone dashboard](https://ryans-paper-desk.enchantingchili2.chatgpt.site)
