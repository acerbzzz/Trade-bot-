# Crypto paper desk

**Monitoring** · Kraken spot · 15-minute candles

Latest completed candle ended **2026-11-26 20:45 UTC**.

| Paper equity | Open positions | Closed trades |
|---:|---:|---:|
| $185.23 | 0 | 46 |

| Market | Last close | Trend | Mean reversion | Breakout | Momentum |
|---|---:|---|---|---|---|
| BTC/USD | $60,716.30 | Waiting | Waiting | Waiting | Waiting |
| ETH/USD | $1,703.10 | Waiting | Waiting | Waiting | Waiting |

## Strategy trials

One independent paper trial per worker minute. Net P&L includes modeled costs.

| Strategy | Closed | Realized P&L | Shortlisted | Next-day validation P&L |
|---|---:|---:|---|---:|
| trend | 12 | $-3.09 | Yes | $+0.00 |
| reversion | 25 | $-1.45 | Yes | $+1.05 |
| breakout | 17 | $-5.72 | Pending | — |
| momentum | 24 | $-13.57 | Yes | $-1.36 |
| relative_strength | 5 | $-7.33 | Pending | — |
| vwap_pullback | 39 | $-14.15 | Pending | — |
| failed_breakdown | 29 | $-8.85 | Yes | $+0.79 |
| grok_pullback | 24 | $-14.99 | Pending | — |
| grok_squeeze | 11 | $-7.90 | Pending | — |
| grok_supertrend | 13 | $+0.87 | Yes | $+2.11 |
| grok_stochastic | 9 | $-1.68 | Yes | $+0.00 |
| grok_confluence | 14 | $+0.31 | Yes | $+1.64 |

Relative strength trial equity: $193.35. 50/50 BTC–ETH buy-and-hold liquidation value: $183.83.

Validation leader: grok_supertrend

Started with $200 simulated USD. Entries and exits are modeled from candles. No broker orders.

[Refresh history](https://github.com/acerbzzz/Trade-bot-/actions/workflows/forward-paper.yml)

Last successful market check: **2026-11-26 20:52 UTC** · Target interval: 1 minute.
Worker started: **2026-11-26 20:00 UTC** · [Worker run](https://github.com/acerbzzz/Trade-bot-/actions/runs/45887816094) · [Restored checkpoint](https://github.com/acerbzzz/Trade-bot-/commit/d3c0f0de1b85c2ff3e726bb0cccfcf90f29abe38)

[Open phone dashboard](https://ryans-paper-desk.enchantingchili2.chatgpt.site)
