# Crypto paper desk

**Monitoring** · Kraken spot · 15-minute candles

Latest completed candle ended **2026-11-27 06:15 UTC**.

| Paper equity | Open positions | Closed trades |
|---:|---:|---:|
| $188.43 | 1 | 48 |

| Market | Last close | Trend | Mean reversion | Breakout | Momentum |
|---|---:|---|---|---|---|
| BTC/USD | $61,838.70 | Waiting | Waiting | In position | Waiting |
| ETH/USD | $1,739.30 | Waiting | Waiting | Waiting | Waiting |

## Strategy trials

One independent paper trial per worker minute. Net P&L includes modeled costs.

| Strategy | Closed | Realized P&L | Shortlisted | Next-day validation P&L |
|---|---:|---:|---|---:|
| trend | 12 | $-3.09 | Yes | $+0.00 |
| reversion | 25 | $-1.45 | Yes | $+1.71 |
| breakout | 18 | $-6.94 | Pending | — |
| momentum | 25 | $-10.08 | Yes | $-1.20 |
| relative_strength | 5 | $-7.33 | Pending | — |
| vwap_pullback | 42 | $-12.33 | Pending | — |
| failed_breakdown | 29 | $-8.85 | Yes | $+0.00 |
| grok_pullback | 24 | $-14.99 | Pending | — |
| grok_squeeze | 11 | $-7.90 | Pending | — |
| grok_supertrend | 15 | $+3.10 | Yes | $-1.52 |
| grok_stochastic | 9 | $-1.68 | Yes | $-0.51 |
| grok_confluence | 15 | $-0.94 | Yes | $-2.31 |

Relative strength trial equity: $195.87. 50/50 BTC–ETH buy-and-hold liquidation value: $187.48.

Validation leader: reversion

Started with $200 simulated USD. Entries and exits are modeled from candles. No broker orders.

[Refresh history](https://github.com/acerbzzz/Trade-bot-/actions/workflows/forward-paper.yml)

Last successful market check: **2026-11-27 06:28 UTC** · Target interval: 1 minute.
Worker started: **2026-11-27 05:00 UTC** · [Worker run](https://github.com/acerbzzz/Trade-bot-/actions/runs/45943185260) · [Restored checkpoint](https://github.com/acerbzzz/Trade-bot-/commit/d6633857f497da9bd87c919b11fc8dbaa46397fc)

[Open phone dashboard](https://ryans-paper-desk.enchantingchili2.chatgpt.site)
