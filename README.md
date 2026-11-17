# Crypto paper desk

**Monitoring** · Kraken spot · 15-minute candles

Latest completed candle ended **2026-11-17 02:00 UTC**.

| Paper equity | Open positions | Closed trades |
|---:|---:|---:|
| $198.62 | 0 | 2 |

| Market | Last close | Trend | Mean reversion | Breakout | Momentum |
|---|---:|---|---|---|---|
| BTC/USD | $64,684.80 | Waiting | Waiting | Waiting | Waiting |
| ETH/USD | $1,819.12 | Waiting | Waiting | Waiting | Waiting |

## Strategy trials

One independent paper trial per worker minute. Net P&L includes modeled costs.

| Strategy | Closed | Realized P&L | Shortlisted | Next-day validation P&L |
|---|---:|---:|---|---:|
| trend | 3 | $-3.26 | Pending | — |
| reversion | 5 | $-1.56 | Pending | — |
| breakout | 4 | $-2.81 | Pending | — |
| momentum | 4 | $-1.57 | Yes | $-1.70 |
| relative_strength | 1 | $-1.50 | Pending | — |
| vwap_pullback | 3 | $-2.50 | Pending | — |
| failed_breakdown | 8 | $+2.15 | Yes | — |
| grok_pullback | 4 | $-4.99 | Pending | — |
| grok_squeeze | 3 | $-2.89 | Pending | — |
| grok_supertrend | 2 | $-1.09 | Yes | $-1.13 |
| grok_stochastic | 1 | $-0.18 | Pending | — |
| grok_confluence | 3 | $-1.71 | Pending | — |

Relative strength trial equity: $198.50. 50/50 BTC–ETH buy-and-hold liquidation value: $196.10.

Validation leader: None profitable

Started with $200 simulated USD. Entries and exits are modeled from candles. No broker orders.

[Refresh history](https://github.com/acerbzzz/Trade-bot-/actions/workflows/forward-paper.yml)

Last successful market check: **2026-11-17 02:13 UTC** · Target interval: 1 minute.
Worker started: **2026-11-17 00:48 UTC** · [Worker run](https://github.com/acerbzzz/Trade-bot-/actions/runs/43990594942) · [Restored checkpoint](https://github.com/acerbzzz/Trade-bot-/commit/f24a8e65593260a0f848b2af98f28486972da661)

[Open phone dashboard](https://ryans-paper-desk.enchantingchili2.chatgpt.site)
