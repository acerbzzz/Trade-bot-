# Crypto paper desk

**Monitoring** · Kraken spot · 15-minute candles

Latest completed candle ended **2026-11-27 09:30 UTC**.

| Paper equity | Open positions | Closed trades |
|---:|---:|---:|
| $187.22 | 0 | 49 |

| Market | Last close | Trend | Mean reversion | Breakout | Momentum |
|---|---:|---|---|---|---|
| BTC/USD | $61,654.60 | Waiting | Waiting | Waiting | Waiting |
| ETH/USD | $1,730.30 | Waiting | Waiting | Waiting | Waiting |

## Strategy trials

One independent paper trial per worker minute. Net P&L includes modeled costs.

| Strategy | Closed | Realized P&L | Shortlisted | Next-day validation P&L |
|---|---:|---:|---|---:|
| trend | 12 | $-3.09 | Yes | $+0.00 |
| reversion | 25 | $-1.45 | Yes | $+1.71 |
| breakout | 19 | $-6.45 | Pending | — |
| momentum | 25 | $-10.08 | Yes | $-1.20 |
| relative_strength | 6 | $-3.72 | Pending | — |
| vwap_pullback | 42 | $-12.33 | Pending | — |
| failed_breakdown | 29 | $-8.85 | Yes | $+0.00 |
| grok_pullback | 25 | $-15.84 | Pending | — |
| grok_squeeze | 11 | $-7.90 | Pending | — |
| grok_supertrend | 15 | $+3.10 | Yes | $-1.52 |
| grok_stochastic | 10 | $-2.57 | Yes | $-0.51 |
| grok_confluence | 16 | $-0.44 | Yes | $-2.31 |

Relative strength trial equity: $196.28. 50/50 BTC–ETH buy-and-hold liquidation value: $186.72.

Validation leader: reversion

Started with $200 simulated USD. Entries and exits are modeled from candles. No broker orders.

[Refresh history](https://github.com/acerbzzz/Trade-bot-/actions/workflows/forward-paper.yml)

Last successful market check: **2026-11-27 09:36 UTC** · Target interval: 1 minute.
Worker started: **2026-11-27 09:30 UTC** · [Worker run](https://github.com/acerbzzz/Trade-bot-/actions/runs/45974274070) · [Restored checkpoint](https://github.com/acerbzzz/Trade-bot-/commit/8d79505bcbc387d51052069f1cc8fd7a2cbf3401)

[Open phone dashboard](https://ryans-paper-desk.enchantingchili2.chatgpt.site)
