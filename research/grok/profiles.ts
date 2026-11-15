import type { Config, Market, Params, StrategyName, Timeframe } from "./types";

export const MINUTES: Record<Timeframe, number> = { "5m": 5, "15m": 15, "1h": 60 };

export const DEFAULT_PARAMS: Params = {
  fast: 12,
  slow: 26,
  adx: 14,
  strength: 20,
  bands: 20,
  deviations: 2,
  rsi: 14,
  oversold: 30,
  recovery: 50,
  channel: 20,
  volumeRatio: 1.2,
  breakoutAtr: 0.1,
  signal: 9,
  momentum: 55,
  stoch: 14,
  stochSmooth: 3,
  keltner: 1.5,
  supertrend: 3,
  votes: 2,
};

export const STRATEGIES: { id: StrategyName; label: string; blurb: string }[] = [
  {
    id: "confluence",
    label: "Confluence",
    blurb: "Long only when at least two of trend, pullback, breakout, momentum, and supertrend agree. Leaves when two agree to exit.",
  },
  {
    id: "trend",
    label: "Trend",
    blurb: "Fast EMA crosses above the slow EMA while ADX clears the strength line.",
  },
  {
    id: "pullback",
    label: "Pullback",
    blurb: "Buys a tag of the fast EMA only while the slow EMA is still rising.",
  },
  {
    id: "breakout",
    label: "Breakout",
    blurb: "Close through the prior channel plus an ATR buffer, on heavier-than-usual volume.",
  },
  {
    id: "squeeze",
    label: "Squeeze",
    blurb: "Bollinger bands sit inside the Keltner channels, then price leaves through the upper band.",
  },
  {
    id: "momentum",
    label: "Momentum",
    blurb: "MACD histogram crosses above zero with RSI already in momentum territory.",
  },
  {
    id: "supertrend",
    label: "Supertrend",
    blurb: "Flips long when price reclaims the ATR trailing band, and flips out when it loses it.",
  },
  {
    id: "reversion",
    label: "Reversion",
    blurb: "Buys a close under the lower Bollinger band when RSI is washed out.",
  },
  {
    id: "stochastic",
    label: "Stochastic",
    blurb: "Bullish stochastic cross out of oversold, and only if price is still above the slow EMA.",
  },
];

const BOOKS: Record<Market, { venue: string; symbols: Record<string, number>; feeBps: number; slipBps: number }> = {
  crypto: {
    venue: "binance",
    symbols: { "BTC/USDT": 0.00001, "ETH/USDT": 0.0001, "SOL/USDT": 0.001 },
    feeBps: 5,
    slipBps: 3,
  },
  stocks: {
    venue: "alpaca",
    symbols: { SPY: 0.001, QQQ: 0.001, AAPL: 0.001 },
    feeBps: 1,
    slipBps: 3,
  },
  forex: {
    venue: "oanda",
    symbols: { "EUR/USD": 1, "GBP/USD": 1, "USD/JPY": 1 },
    feeBps: 1,
    slipBps: 2,
  },
};

export function minWarmup(params: Params, corrWindow: number, atrPeriod: number): number {
  return (
    Math.max(2 * params.adx, params.slow + params.signal, params.channel, params.bands, params.rsi, params.stoch + params.stochSmooth, corrWindow, atrPeriod) +
    3
  );
}

export function makeConfig(input: {
  market: Market;
  timeframe: Timeframe;
  strategy: StrategyName;
  risk: number;
  atrStop: number;
  votes: number;
  wholeShares: boolean;
}): Config {
  const book = BOOKS[input.market];
  const symbols = { ...book.symbols };
  if (input.market === "stocks" && input.wholeShares) {
    for (const key of Object.keys(symbols)) symbols[key] = 1;
  }
  const votes = Math.min(4, Math.max(2, Math.round(input.votes)));
  return {
    market: input.market,
    venue: book.venue,
    strategy: input.strategy,
    equity: 200,
    timeframe: input.timeframe,
    risk: input.risk,
    reward: 2.5,
    atrPeriod: 14,
    atrStop: input.atrStop,
    maxPositions: 2,
    dailyLoss: 0.03,
    drawdown: 0.1,
    correlation: 0.8,
    corrWindow: 40,
    feeBps: book.feeBps,
    slipBps: book.slipBps,
    history: 300,
    pollSeconds: 30,
    holdout: 0.3,
    wholeShares: input.wholeShares,
    params: { ...DEFAULT_PARAMS, votes },
    symbols,
  };
}
