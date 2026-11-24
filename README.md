# Crypto paper desk

**Monitoring** · Kraken spot · 15-minute candles

Latest completed candle ended **2026-11-24 13:30 UTC**.

| Paper equity | Open positions | Closed trades |
|---:|---:|---:|
| $186.39 | 0 | 37 |

| Market | Last close | Trend | Mean reversion | Breakout | Momentum |
|---|---:|---|---|---|---|
| BTC/USD | $60,052.20 | Waiting | Waiting | Waiting | Waiting |
| ETH/USD | $1,691.31 | Waiting | Waiting | Waiting | Waiting |

## Strategy trials

One independent paper trial per worker minute. Net P&L includes modeled costs.

| Strategy | Closed | Realized P&L | Shortlisted | Next-day validation P&L |
|---|---:|---:|---|---:|
| trend | 11 | $-1.60 | Yes | $-0.57 |
| reversion | 20 | $-4.16 | Yes | $+0.00 |
| breakout | 16 | $-7.40 | Pending | — |
| momentum | 19 | $-9.68 | Yes | $-3.21 |
| relative_strength | 5 | $-7.33 | Pending | — |
| vwap_pullback | 29 | $-9.26 | Pending | — |
| failed_breakdown | 22 | $-7.06 | Yes | $+0.00 |
| grok_pullback | 20 | $-11.82 | Pending | — |
| grok_squeeze | 10 | $-7.41 | Pending | — |
| grok_supertrend | 12 | $-0.33 | Yes | $+3.73 |
| grok_stochastic | 8 | $-1.17 | Yes | $-1.81 |
| grok_confluence | 10 | $+1.35 | Yes | $-2.05 |

Relative strength trial equity: $192.67. 50/50 BTC–ETH buy-and-hold liquidation value: $181.63.

Validation leader: grok_supertrend

Started with $200 simulated USD. Entries and exits are modeled from candles. No broker orders.

[Refresh history](https://github.com/acerbzzz/Trade-bot-/actions/workflows/forward-paper.yml)

Last successful market check: **2026-11-24 13:31 UTC** · Target interval: 1 minute.
Worker started: **2026-11-24 13:04 UTC** · [Worker run](https://github.com/acerbzzz/Trade-bot-/actions/runs/45399678474) · [Restored checkpoint](https://github.com/acerbzzz/Trade-bot-/commit/5f0f38265b2394b60bd248da5385f83123e03617)

[Open phone dashboard](https://ryans-paper-desk.enchantingchili2.chatgpt.site)
