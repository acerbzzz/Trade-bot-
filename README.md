# Crypto paper desk

**Monitoring** · Kraken spot · 15-minute candles

Latest completed candle ended **2026-11-26 01:45 UTC**.

| Paper equity | Open positions | Closed trades |
|---:|---:|---:|
| $186.32 | 1 | 41 |

| Market | Last close | Trend | Mean reversion | Breakout | Momentum |
|---|---:|---|---|---|---|
| BTC/USD | $60,704.10 | Waiting | Waiting | Waiting | In position |
| ETH/USD | $1,699.35 | Waiting | Waiting | Waiting | Waiting |

## Strategy trials

One independent paper trial per worker minute. Net P&L includes modeled costs.

| Strategy | Closed | Realized P&L | Shortlisted | Next-day validation P&L |
|---|---:|---:|---|---:|
| trend | 12 | $-3.09 | Yes | $-2.99 |
| reversion | 24 | $-3.13 | Yes | $+0.46 |
| breakout | 17 | $-5.72 | Pending | — |
| momentum | 20 | $-10.78 | Yes | $-1.50 |
| relative_strength | 5 | $-7.33 | Pending | — |
| vwap_pullback | 33 | $-9.54 | Pending | — |
| failed_breakdown | 29 | $-8.85 | Yes | $-4.65 |
| grok_pullback | 21 | $-12.92 | Pending | — |
| grok_squeeze | 10 | $-7.41 | Pending | — |
| grok_supertrend | 12 | $-0.33 | Yes | $-1.50 |
| grok_stochastic | 8 | $-1.17 | Yes | $+0.00 |
| grok_confluence | 12 | $+1.74 | Yes | $-2.66 |

Relative strength trial equity: $193.32. 50/50 BTC–ETH buy-and-hold liquidation value: $183.61.

Validation leader: reversion

Started with $200 simulated USD. Entries and exits are modeled from candles. No broker orders.

[Refresh history](https://github.com/acerbzzz/Trade-bot-/actions/workflows/forward-paper.yml)

Last successful market check: **2026-11-26 01:48 UTC** · Target interval: 1 minute.
Worker started: **2026-11-26 00:31 UTC** · [Worker run](https://github.com/acerbzzz/Trade-bot-/actions/runs/45729221340) · [Restored checkpoint](https://github.com/acerbzzz/Trade-bot-/commit/2b7d710b176aaac79703f57585aeef49b62d23ec)

[Open phone dashboard](https://ryans-paper-desk.enchantingchili2.chatgpt.site)
