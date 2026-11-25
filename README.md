# Crypto paper desk

**Monitoring** · Kraken spot · 15-minute candles

Latest completed candle ended **2026-11-25 10:45 UTC**.

| Paper equity | Open positions | Closed trades |
|---:|---:|---:|
| $186.44 | 0 | 38 |

| Market | Last close | Trend | Mean reversion | Breakout | Momentum |
|---|---:|---|---|---|---|
| BTC/USD | $58,865.40 | Waiting | Waiting | Waiting | Waiting |
| ETH/USD | $1,643.57 | Waiting | Waiting | Waiting | Waiting |

## Strategy trials

One independent paper trial per worker minute. Net P&L includes modeled costs.

| Strategy | Closed | Realized P&L | Shortlisted | Next-day validation P&L |
|---|---:|---:|---|---:|
| trend | 12 | $-3.09 | Yes | $-2.99 |
| reversion | 21 | $-4.12 | Yes | $+0.46 |
| breakout | 16 | $-7.40 | Pending | — |
| momentum | 19 | $-9.68 | Yes | $-1.50 |
| relative_strength | 5 | $-7.33 | Pending | — |
| vwap_pullback | 31 | $-10.53 | Pending | — |
| failed_breakdown | 26 | $-11.47 | Yes | $-4.65 |
| grok_pullback | 21 | $-12.92 | Pending | — |
| grok_squeeze | 10 | $-7.41 | Pending | — |
| grok_supertrend | 12 | $-0.33 | Yes | $-1.50 |
| grok_stochastic | 8 | $-1.17 | Yes | $+0.00 |
| grok_confluence | 11 | $+0.17 | Yes | $-2.66 |

Relative strength trial equity: $192.67. 50/50 BTC–ETH buy-and-hold liquidation value: $177.82.

Validation leader: reversion

Started with $200 simulated USD. Entries and exits are modeled from candles. No broker orders.

[Refresh history](https://github.com/acerbzzz/Trade-bot-/actions/workflows/forward-paper.yml)

Last successful market check: **2026-11-25 10:58 UTC** · Target interval: 1 minute.
Worker started: **2026-11-25 10:26 UTC** · [Worker run](https://github.com/acerbzzz/Trade-bot-/actions/runs/45595004956) · [Restored checkpoint](https://github.com/acerbzzz/Trade-bot-/commit/0d663c04d69f5d26bbd79f74f142179f6bb57ca3)

[Open phone dashboard](https://ryans-paper-desk.enchantingchili2.chatgpt.site)
