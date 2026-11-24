# Crypto paper desk

**Monitoring** · Kraken spot · 15-minute candles

Latest completed candle ended **2026-11-24 19:15 UTC**.

| Paper equity | Open positions | Closed trades |
|---:|---:|---:|
| $186.39 | 0 | 37 |

| Market | Last close | Trend | Mean reversion | Breakout | Momentum |
|---|---:|---|---|---|---|
| BTC/USD | $59,884.90 | Waiting | Waiting | Waiting | Waiting |
| ETH/USD | $1,679.08 | Waiting | Waiting | Waiting | Waiting |

## Strategy trials

One independent paper trial per worker minute. Net P&L includes modeled costs.

| Strategy | Closed | Realized P&L | Shortlisted | Next-day validation P&L |
|---|---:|---:|---|---:|
| trend | 12 | $-3.09 | Yes | $-0.57 |
| reversion | 20 | $-4.16 | Yes | $+0.00 |
| breakout | 16 | $-7.40 | Pending | — |
| momentum | 19 | $-9.68 | Yes | $-3.21 |
| relative_strength | 5 | $-7.33 | Pending | — |
| vwap_pullback | 31 | $-10.53 | Pending | — |
| failed_breakdown | 23 | $-8.16 | Yes | $+0.00 |
| grok_pullback | 21 | $-12.92 | Pending | — |
| grok_squeeze | 10 | $-7.41 | Pending | — |
| grok_supertrend | 12 | $-0.33 | Yes | $+3.73 |
| grok_stochastic | 8 | $-1.17 | Yes | $-1.81 |
| grok_confluence | 11 | $+0.17 | Yes | $-2.05 |

Relative strength trial equity: $192.67. 50/50 BTC–ETH buy-and-hold liquidation value: $181.28.

Validation leader: grok_supertrend

Started with $200 simulated USD. Entries and exits are modeled from candles. No broker orders.

[Refresh history](https://github.com/acerbzzz/Trade-bot-/actions/workflows/forward-paper.yml)

Last successful market check: **2026-11-24 19:23 UTC** · Target interval: 1 minute.
Worker started: **2026-11-24 19:20 UTC** · [Worker run](https://github.com/acerbzzz/Trade-bot-/actions/runs/45469168338) · [Restored checkpoint](https://github.com/acerbzzz/Trade-bot-/commit/589da3e5114a1167961e5804bfcb006c84792a59)

[Open phone dashboard](https://ryans-paper-desk.enchantingchili2.chatgpt.site)
