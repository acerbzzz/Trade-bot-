# Crypto paper desk

**Monitoring** · Kraken spot · 15-minute candles

Latest completed candle ended **2026-11-25 23:00 UTC**.

| Paper equity | Open positions | Closed trades |
|---:|---:|---:|
| $187.24 | 0 | 40 |

| Market | Last close | Trend | Mean reversion | Breakout | Momentum |
|---|---:|---|---|---|---|
| BTC/USD | $60,018.00 | Waiting | Waiting | Waiting | Waiting |
| ETH/USD | $1,684.17 | Waiting | Waiting | Waiting | Waiting |

## Strategy trials

One independent paper trial per worker minute. Net P&L includes modeled costs.

| Strategy | Closed | Realized P&L | Shortlisted | Next-day validation P&L |
|---|---:|---:|---|---:|
| trend | 12 | $-3.09 | Yes | $-2.99 |
| reversion | 24 | $-3.13 | Yes | $+0.46 |
| breakout | 16 | $-7.40 | Pending | — |
| momentum | 19 | $-9.68 | Yes | $-1.50 |
| relative_strength | 5 | $-7.33 | Pending | — |
| vwap_pullback | 32 | $-11.40 | Pending | — |
| failed_breakdown | 29 | $-8.85 | Yes | $-4.65 |
| grok_pullback | 21 | $-12.92 | Pending | — |
| grok_squeeze | 10 | $-7.41 | Pending | — |
| grok_supertrend | 12 | $-0.33 | Yes | $-1.50 |
| grok_stochastic | 8 | $-1.17 | Yes | $+0.00 |
| grok_confluence | 11 | $+0.17 | Yes | $-2.66 |

Relative strength trial equity: $192.67. 50/50 BTC–ETH buy-and-hold liquidation value: $181.75.

Validation leader: reversion

Started with $200 simulated USD. Entries and exits are modeled from candles. No broker orders.

[Refresh history](https://github.com/acerbzzz/Trade-bot-/actions/workflows/forward-paper.yml)

Last successful market check: **2026-11-25 23:01 UTC** · Target interval: 1 minute.
Worker started: **2026-11-25 23:00 UTC** · [Worker run](https://github.com/acerbzzz/Trade-bot-/actions/runs/45717901831) · [Restored checkpoint](https://github.com/acerbzzz/Trade-bot-/commit/e65ecd394df14dc13d52e1779def0876e5d6f796)

[Open phone dashboard](https://ryans-paper-desk.enchantingchili2.chatgpt.site)
