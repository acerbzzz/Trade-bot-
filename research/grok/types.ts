export type Market = "crypto" | "stocks" | "forex";
export type Timeframe = "5m" | "15m" | "1h";
export type StrategyName =
  | "confluence"
  | "trend"
  | "pullback"
  | "breakout"
  | "squeeze"
  | "momentum"
  | "supertrend"
  | "reversion"
  | "stochastic";

export type Bar = {
  t: number;
  open: number;
  high: number;
  low: number;
  close: number;
  volume: number;
};

export type Params = {
  fast: number;
  slow: number;
  adx: number;
  strength: number;
  bands: number;
  deviations: number;
  rsi: number;
  oversold: number;
  recovery: number;
  channel: number;
  volumeRatio: number;
  breakoutAtr: number;
  signal: number;
  momentum: number;
  stoch: number;
  stochSmooth: number;
  keltner: number;
  supertrend: number;
  votes: number;
};

export type Config = {
  market: Market;
  venue: string;
  strategy: StrategyName;
  equity: number;
  timeframe: Timeframe;
  risk: number;
  reward: number;
  atrPeriod: number;
  atrStop: number;
  maxPositions: number;
  dailyLoss: number;
  drawdown: number;
  correlation: number;
  corrWindow: number;
  feeBps: number;
  slipBps: number;
  history: number;
  pollSeconds: number;
  holdout: number;
  wholeShares: boolean;
  params: Params;
  symbols: Record<string, number>;
};

export type Frame = Bar & {
  atr: number | null;
  enter: boolean;
  exit: boolean;
  fast: number | null;
  slow: number | null;
  adx: number | null;
  rsi: number | null;
  mid: number | null;
  upper: number | null;
  lower: number | null;
  hist: number | null;
  channelHigh: number | null;
  channelLow: number | null;
  stochK: number | null;
  stochD: number | null;
  super: number | null;
  superUp: boolean;
  kUpper: number | null;
  kLower: number | null;
  squeeze: boolean;
};

export type RawFrame = Omit<Frame, "enter" | "exit">;

export type Position = {
  entry: number;
  qty: number;
  stop: number;
  target: number;
  capital: number;
  opened: string;
  riskUsd: number;
};

export type Account = {
  balance: number;
  equity: number;
  peak: number;
  dayStart: number;
  day: string;
  halted: boolean;
  dayHalt: boolean;
  positions: Record<string, Position>;
  cursor: string | null;
};

export type Trade = {
  symbol: string;
  opened: string;
  closed: string;
  qty: number;
  entry: number;
  exit: number;
  pnl: number;
  reason: string;
  r: number | null;
};

export type Skip = {
  symbol: string;
  time: string;
  reason: string;
};

export type CurvePoint = {
  t: number;
  equity: number;
  bench: number;
};

export type Run = {
  account: Account;
  trades: Trade[];
  skips: Skip[];
  curve: CurvePoint[];
  cursorIndex: number;
  flattened: boolean;
};

export type BookPayload = {
  market: Market;
  timeframe: Timeframe;
  source: "binance" | "yahoo" | "synthetic";
  sourceLabel: string;
  note: string;
  symbols: string[];
  bars: Record<string, Bar[]>;
};

export type Side = { enter: boolean; exit: boolean };
