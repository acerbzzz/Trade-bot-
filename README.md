# Crypto paper desk

**Monitoring** · Kraken spot · 15-minute candles

Latest completed candle ended **2026-11-22 01:30 UTC**.

| Paper equity | Open positions | Closed trades |
|---:|---:|---:|
| $193.66 | 0 | 24 |

| Market | Last close | Trend | Mean reversion | Breakout | Momentum |
|---|---:|---|---|---|---|
| BTC/USD | $60,001.50 | Waiting | Waiting | Waiting | Waiting |
| ETH/USD | $1,681.44 | Waiting | Waiting | Waiting | Waiting |

## Strategy trials

One independent paper trial per worker minute. Net P&L includes modeled costs.

| Strategy | Closed | Realized P&L | Shortlisted | Next-day validation P&L |
|---|---:|---:|---|---:|
| trend | 6 | $-5.99 | Pending | — |
| reversion | 16 | $-1.73 | Yes | $+0.35 |
| breakout | 11 | $-6.28 | Pending | — |
| momentum | 11 | $-2.47 | Yes | $+3.74 |
| relative_strength | 2 | $-2.99 | Pending | — |
| vwap_pullback | 20 | $-7.32 | Pending | — |
| failed_breakdown | 20 | $-4.14 | Yes | $+2.21 |
| grok_pullback | 12 | $-6.78 | Pending | — |
| grok_squeeze | 7 | $-3.83 | Pending | — |
| grok_supertrend | 9 | $-6.16 | Yes | $+3.75 |
| grok_stochastic | 2 | $-0.32 | Pending | — |
| grok_confluence | 6 | $+1.20 | Yes | — |

Relative strength trial equity: $196.87. 50/50 BTC–ETH buy-and-hold liquidation value: $181.75.

Validation leader: grok_supertrend

Started with $200 simulated USD. Entries and exits are modeled from candles. No broker orders.

[Refresh history](https://github.com/acerbzzz/Trade-bot-/actions/workflows/forward-paper.yml)

Last successful market check: **2026-11-22 01:33 UTC** · Target interval: 1 minute.
Worker started: **2026-11-22 00:49 UTC** · [Worker run](https://github.com/acerbzzz/Trade-bot-/actions/runs/44968488380) · [Restored checkpoint](https://github.com/acerbzzz/Trade-bot-/commit/eb82efd4a6d6f0cff58699f89a04754eb4fbf13c)

[Open phone dashboard](https://ryans-paper-desk.enchantingchili2.chatgpt.site)
