# Crypto paper desk

**Monitoring** · Kraken spot · 15-minute candles

Latest completed candle ended **2026-11-24 06:45 UTC**.

| Paper equity | Open positions | Closed trades |
|---:|---:|---:|
| $187.80 | 0 | 36 |

| Market | Last close | Trend | Mean reversion | Breakout | Momentum |
|---|---:|---|---|---|---|
| BTC/USD | $60,402.40 | Waiting | Waiting | Waiting | Waiting |
| ETH/USD | $1,699.18 | Waiting | Waiting | Waiting | Waiting |

## Strategy trials

One independent paper trial per worker minute. Net P&L includes modeled costs.

| Strategy | Closed | Realized P&L | Shortlisted | Next-day validation P&L |
|---|---:|---:|---|---:|
| trend | 10 | $-0.10 | Yes | $-0.57 |
| reversion | 20 | $-4.16 | Yes | $+0.00 |
| breakout | 16 | $-7.40 | Pending | — |
| momentum | 18 | $-8.25 | Yes | $-3.21 |
| relative_strength | 5 | $-7.33 | Pending | — |
| vwap_pullback | 28 | $-9.06 | Pending | — |
| failed_breakdown | 21 | $-5.61 | Yes | $+0.00 |
| grok_pullback | 20 | $-11.82 | Pending | — |
| grok_squeeze | 10 | $-7.41 | Pending | — |
| grok_supertrend | 11 | $+1.17 | Yes | $+3.73 |
| grok_stochastic | 8 | $-1.17 | Yes | $-1.81 |
| grok_confluence | 9 | $+2.86 | Yes | $-2.05 |

Relative strength trial equity: $192.67. 50/50 BTC–ETH buy-and-hold liquidation value: $183.09.

Validation leader: grok_supertrend

Started with $200 simulated USD. Entries and exits are modeled from candles. No broker orders.

[Refresh history](https://github.com/acerbzzz/Trade-bot-/actions/workflows/forward-paper.yml)

Last successful market check: **2026-11-24 06:48 UTC** · Target interval: 1 minute.
Worker started: **2026-11-24 05:34 UTC** · [Worker run](https://github.com/acerbzzz/Trade-bot-/actions/runs/45334265597) · [Restored checkpoint](https://github.com/acerbzzz/Trade-bot-/commit/be0d322d42f4123f9a73f6ea74528d06f7dc6bf9)

[Open phone dashboard](https://ryans-paper-desk.enchantingchili2.chatgpt.site)
