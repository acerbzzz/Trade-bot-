# Crypto paper desk

**Monitoring** · Kraken spot · 15-minute candles

Latest completed candle ended **2026-11-27 08:15 UTC**.

| Paper equity | Open positions | Closed trades |
|---:|---:|---:|
| $187.22 | 0 | 49 |

| Market | Last close | Trend | Mean reversion | Breakout | Momentum |
|---|---:|---|---|---|---|
| BTC/USD | $61,794.10 | Waiting | Waiting | Waiting | Waiting |
| ETH/USD | $1,733.74 | Waiting | Waiting | Waiting | Waiting |

## Strategy trials

One independent paper trial per worker minute. Net P&L includes modeled costs.

| Strategy | Closed | Realized P&L | Shortlisted | Next-day validation P&L |
|---|---:|---:|---|---:|
| trend | 12 | $-3.09 | Yes | $+0.00 |
| reversion | 25 | $-1.45 | Yes | $+1.71 |
| breakout | 19 | $-6.45 | Pending | — |
| momentum | 25 | $-10.08 | Yes | $-1.20 |
| relative_strength | 5 | $-7.33 | Pending | — |
| vwap_pullback | 42 | $-12.33 | Pending | — |
| failed_breakdown | 29 | $-8.85 | Yes | $+0.00 |
| grok_pullback | 25 | $-15.84 | Pending | — |
| grok_squeeze | 11 | $-7.90 | Pending | — |
| grok_supertrend | 15 | $+3.10 | Yes | $-1.52 |
| grok_stochastic | 10 | $-2.57 | Yes | $-0.51 |
| grok_confluence | 16 | $-0.44 | Yes | $-2.31 |

Relative strength trial equity: $195.77. 50/50 BTC–ETH buy-and-hold liquidation value: $187.12.

Validation leader: reversion

Started with $200 simulated USD. Entries and exits are modeled from candles. No broker orders.

[Refresh history](https://github.com/acerbzzz/Trade-bot-/actions/workflows/forward-paper.yml)

Last successful market check: **2026-11-27 08:29 UTC** · Target interval: 1 minute.
Worker started: **2026-11-27 08:00 UTC** · [Worker run](https://github.com/acerbzzz/Trade-bot-/actions/runs/45962382049) · [Restored checkpoint](https://github.com/acerbzzz/Trade-bot-/commit/9859533cf8b22f1d590359f1ec9e0d5e69ab1af7)

[Open phone dashboard](https://ryans-paper-desk.enchantingchili2.chatgpt.site)
