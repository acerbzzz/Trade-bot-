# Crypto paper desk

**Monitoring** · Kraken spot · 15-minute candles

Latest completed candle ended **2026-11-15 15:30 UTC**.

| Paper equity | Open positions | Closed trades |
|---:|---:|---:|
| $199.72 | 0 | 1 |

| Market | Last close | Trend | Mean reversion | Breakout | Momentum |
|---|---:|---|---|---|---|
| BTC/USD | $64,597.60 | Waiting | Waiting | Waiting | Waiting |
| ETH/USD | $1,808.39 | Waiting | Waiting | Waiting | Waiting |

## Strategy trials

One independent paper trial per worker minute. Net P&L includes modeled costs.

| Strategy | Closed | Realized P&L | Shortlisted | Next-day validation P&L |
|---|---:|---:|---|---:|
| trend | 1 | $-1.50 | Pending | — |
| reversion | 5 | $-1.56 | Pending | — |
| breakout | 2 | $-0.49 | Pending | — |
| momentum | 1 | $+0.06 | Yes | — |
| relative_strength | 0 | $+0.00 | Pending | — |
| vwap_pullback | — | — | Awaiting first test | — |
| failed_breakdown | — | — | Awaiting first test | — |

Relative strength trial equity: $200.00. 50/50 BTC–ETH buy-and-hold liquidation value: $195.39.

Started with $200 simulated USD. Entries and exits are modeled from candles. No broker orders.

[Refresh history](https://github.com/acerbzzz/Trade-bot-/actions/workflows/forward-paper.yml)

Last successful market check: **2026-11-15 15:36 UTC** · Target interval: 1 minute.
