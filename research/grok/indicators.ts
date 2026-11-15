import type { Bar, Frame, Params, RawFrame, Side, StrategyName } from "./types";

function ewm(values: (number | null)[], span: number, alpha: number): (number | null)[] {
  const out: (number | null)[] = [];
  let prev: number | null = null;
  let seen = 0;
  for (const x of values) {
    if (x == null || !Number.isFinite(x)) {
      out.push(null);
      continue;
    }
    seen += 1;
    prev = prev == null ? x : (1 - alpha) * prev + alpha * x;
    out.push(seen >= span ? prev : null);
  }
  return out;
}

function ema(values: number[], span: number): (number | null)[] {
  return ewm(values, span, 2 / (span + 1));
}

function wilder(values: (number | null)[], period: number): (number | null)[] {
  return ewm(values, period, 1 / period);
}

function rollingMean(values: number[], n: number): (number | null)[] {
  const out: (number | null)[] = [];
  let sum = 0;
  for (let i = 0; i < values.length; i++) {
    sum += values[i];
    if (i >= n) sum -= values[i - n];
    out.push(i >= n - 1 ? sum / n : null);
  }
  return out;
}

function rollingStd(values: number[], n: number): (number | null)[] {
  const out: (number | null)[] = [];
  for (let i = 0; i < values.length; i++) {
    if (i < n - 1) {
      out.push(null);
      continue;
    }
    let sum = 0;
    for (let k = i - n + 1; k <= i; k++) sum += values[k];
    const mean = sum / n;
    let v = 0;
    for (let k = i - n + 1; k <= i; k++) {
      const d = values[k] - mean;
      v += d * d;
    }
    out.push(Math.sqrt(v / n));
  }
  return out;
}

function rollShift(values: number[], n: number, fn: (window: number[]) => number): (number | null)[] {
  const out: (number | null)[] = new Array(values.length).fill(null);
  for (let i = n; i < values.length; i++) {
    const window: number[] = [];
    for (let k = i - n; k <= i - 1; k++) window.push(values[k]);
    out[i] = fn(window);
  }
  return out;
}

function trueRange(bars: Bar[]): number[] {
  return bars.map((bar, i) => {
    if (i === 0) return bar.high - bar.low;
    const prev = bars[i - 1].close;
    return Math.max(bar.high - bar.low, Math.abs(bar.high - prev), Math.abs(bar.low - prev));
  });
}

function rsi(closes: number[], period: number): (number | null)[] {
  const up: (number | null)[] = [null];
  const down: (number | null)[] = [null];
  for (let i = 1; i < closes.length; i++) {
    const d = closes[i] - closes[i - 1];
    up.push(d > 0 ? d : 0);
    down.push(d < 0 ? -d : 0);
  }
  const avgUp = wilder(up, period);
  const avgDown = wilder(down, period);
  return avgUp.map((u, i) => {
    const d = avgDown[i];
    if (u == null || d == null) return null;
    if (d === 0) return 100;
    return 100 - 100 / (1 + u / d);
  });
}

function adx(bars: Bar[], period: number): (number | null)[] {
  const plus: (number | null)[] = [null];
  const minus: (number | null)[] = [null];
  for (let i = 1; i < bars.length; i++) {
    const up = bars[i].high - bars[i - 1].high;
    const down = bars[i - 1].low - bars[i].low;
    plus.push(up > down && up > 0 ? up : 0);
    minus.push(down > up && down > 0 ? down : 0);
  }
  const atr = wilder(trueRange(bars), period);
  const smPlus = wilder(plus, period);
  const smMinus = wilder(minus, period);
  const dx: (number | null)[] = atr.map((a, i) => {
    const p = smPlus[i];
    const m = smMinus[i];
    if (a == null || p == null || m == null || a === 0 || p + m === 0) return null;
    const pdi = (100 * p) / a;
    const mdi = (100 * m) / a;
    return (100 * Math.abs(pdi - mdi)) / (pdi + mdi);
  });
  return wilder(dx, period);
}

function macdHist(closes: number[], slow: number, fast: number, signal: number): (number | null)[] {
  const fastE = ema(closes, fast);
  const slowE = ema(closes, slow);
  const line = fastE.map((f, i) => (f == null || slowE[i] == null ? null : f - (slowE[i] as number)));
  const sig = ewm(line, signal, 2 / (signal + 1));
  return line.map((v, i) => (v == null || sig[i] == null ? null : v - (sig[i] as number)));
}

function stochastic(bars: Bar[], kPeriod: number, dPeriod: number): { k: (number | null)[]; d: (number | null)[] } {
  const k: (number | null)[] = [];
  for (let i = 0; i < bars.length; i++) {
    if (i < kPeriod - 1) {
      k.push(null);
      continue;
    }
    let hh = -Infinity;
    let ll = Infinity;
    for (let j = i - kPeriod + 1; j <= i; j++) {
      hh = Math.max(hh, bars[j].high);
      ll = Math.min(ll, bars[j].low);
    }
    k.push(hh === ll ? 50 : (100 * (bars[i].close - ll)) / (hh - ll));
  }
  const d = k.map((_, i) => {
    if (i < kPeriod - 1 + dPeriod - 1) return null;
    let sum = 0;
    for (let j = i - dPeriod + 1; j <= i; j++) {
      if (k[j] == null) return null;
      sum += k[j] as number;
    }
    return sum / dPeriod;
  });
  return { k, d };
}

function supertrend(bars: Bar[], atr: (number | null)[], mult: number): { line: (number | null)[]; up: boolean[] } {
  const line: (number | null)[] = [];
  const up: boolean[] = [];
  let finalUpper = 0;
  let finalLower = 0;
  let bull = false;
  let ready = false;
  for (let i = 0; i < bars.length; i++) {
    const a = atr[i];
    if (a == null) {
      line.push(null);
      up.push(false);
      ready = false;
      continue;
    }
    const hl2 = (bars[i].high + bars[i].low) / 2;
    const basicUpper = hl2 + mult * a;
    const basicLower = hl2 - mult * a;
    if (!ready) {
      finalUpper = basicUpper;
      finalLower = basicLower;
      bull = bars[i].close >= hl2;
      ready = true;
    } else {
      const prevClose = bars[i - 1].close;
      finalUpper = basicUpper < finalUpper || prevClose > finalUpper ? basicUpper : finalUpper;
      finalLower = basicLower > finalLower || prevClose < finalLower ? basicLower : finalLower;
      if (bull && bars[i].close < finalLower) bull = false;
      else if (!bull && bars[i].close > finalUpper) bull = true;
    }
    line.push(bull ? finalLower : finalUpper);
    up.push(bull);
  }
  return { line, up };
}

export function enrich(bars: Bar[], params: Params, atrPeriod: number): RawFrame[] {
  const closes = bars.map((b) => b.close);
  const fast = ema(closes, params.fast);
  const slow = ema(closes, params.slow);
  const adxLine = adx(bars, params.adx);
  const rsiLine = rsi(closes, params.rsi);
  const mid = rollingMean(closes, params.bands);
  const std = rollingStd(closes, params.bands);
  const kMid = ema(closes, params.bands);
  const atr = wilder(trueRange(bars), atrPeriod);
  const upper = mid.map((m, i) => (m == null || std[i] == null ? null : m + params.deviations * (std[i] as number)));
  const lower = mid.map((m, i) => (m == null || std[i] == null ? null : m - params.deviations * (std[i] as number)));
  const hist = macdHist(closes, params.slow, params.fast, params.signal);
  const highs = bars.map((b) => b.high);
  const lows = bars.map((b) => b.low);
  const channelHigh = rollShift(highs, params.channel, (w) => Math.max(...w));
  const channelLow = rollShift(lows, params.channel, (w) => Math.min(...w));
  const stoch = stochastic(bars, params.stoch, params.stochSmooth);
  const st = supertrend(bars, atr, params.supertrend);
  return bars.map((bar, i) => {
    const kUpper = kMid[i] == null || atr[i] == null ? null : (kMid[i] as number) + params.keltner * (atr[i] as number);
    const kLower = kMid[i] == null || atr[i] == null ? null : (kMid[i] as number) - params.keltner * (atr[i] as number);
    const squeeze = Boolean(
      upper[i] != null && lower[i] != null && kUpper != null && kLower != null && (upper[i] as number) < kUpper && (lower[i] as number) > kLower,
    );
    return {
      ...bar,
      atr: atr[i],
      fast: fast[i],
      slow: slow[i],
      adx: adxLine[i],
      rsi: rsiLine[i],
      mid: mid[i],
      upper: upper[i],
      lower: lower[i],
      hist: hist[i],
      channelHigh: channelHigh[i],
      channelLow: channelLow[i],
      stochK: stoch.k[i],
      stochD: stoch.d[i],
      super: st.line[i],
      superUp: st.line[i] != null && st.up[i],
      kUpper,
      kLower,
      squeeze,
    };
  });
}

function volumeOk(volume: number, mean: number | null, ratio: number): boolean {
  return mean != null && mean > 0 && volume > mean * ratio;
}

export function evaluateBar(row: RawFrame, prev: RawFrame | undefined, params: Params, volMean: number | null): Record<StrategyName, Side> {
  const trendEnter = Boolean(
    row.fast != null &&
      row.slow != null &&
      prev?.fast != null &&
      prev.slow != null &&
      row.adx != null &&
      row.fast > row.slow &&
      prev.fast <= prev.slow &&
      row.adx >= params.strength,
  );
  const trendExit = Boolean(row.fast != null && row.slow != null && row.fast < row.slow);

  const pullbackEnter = Boolean(
    prev &&
      row.fast != null &&
      row.slow != null &&
      prev.fast != null &&
      prev.slow != null &&
      row.adx != null &&
      row.fast > row.slow &&
      row.slow > prev.slow &&
      prev.close > prev.fast &&
      row.low <= row.fast &&
      row.close > row.fast &&
      row.adx >= params.strength,
  );
  const pullbackExit = Boolean(row.slow != null && row.close < row.slow);

  const breakoutEnter = Boolean(
    row.channelHigh != null &&
      row.atr != null &&
      row.close > row.channelHigh + params.breakoutAtr * row.atr &&
      volumeOk(row.volume, volMean, params.volumeRatio),
  );
  const breakoutExit = Boolean(
    row.channelHigh != null && row.channelLow != null && row.close < (row.channelHigh + row.channelLow) / 2,
  );

  const squeezeEnter = Boolean(
    prev?.squeeze && row.upper != null && row.close > row.upper && volumeOk(row.volume, volMean, params.volumeRatio),
  );
  const squeezeExit = Boolean(row.mid != null && row.close < row.mid);

  const momentumEnter = Boolean(
    row.hist != null && prev?.hist != null && row.hist > 0 && prev.hist <= 0 && row.rsi != null && row.rsi >= params.momentum,
  );
  const momentumExit = Boolean((row.hist != null && row.hist < 0) || (row.rsi != null && row.rsi < 50));

  const superEnter = Boolean(prev?.super != null && row.super != null && !prev.superUp && row.superUp);
  const superExit = Boolean(prev?.super != null && row.super != null && prev.superUp && !row.superUp);

  const reversionEnter = Boolean(row.lower != null && row.rsi != null && row.close < row.lower && row.rsi < params.oversold);
  const reversionExit = Boolean((row.mid != null && row.close >= row.mid) || (row.rsi != null && row.rsi >= params.recovery));

  const stochasticEnter = Boolean(
    prev?.stochK != null &&
      prev.stochD != null &&
      row.stochK != null &&
      row.stochD != null &&
      prev.stochK <= prev.stochD &&
      row.stochK > row.stochD &&
      row.stochK < params.oversold + 10 &&
      row.slow != null &&
      row.close > row.slow,
  );
  const stochasticExit = Boolean(
    (row.stochK != null && row.stochD != null && row.stochK < row.stochD && row.stochK > 70) ||
      (row.slow != null && row.close < row.slow),
  );

  const directional = [
    { enter: trendEnter, exit: trendExit },
    { enter: pullbackEnter, exit: pullbackExit },
    { enter: breakoutEnter, exit: breakoutExit },
    { enter: momentumEnter, exit: momentumExit },
    { enter: superEnter, exit: superExit },
  ];
  const bulls = directional.filter((s) => s.enter).length;
  const bears = directional.filter((s) => s.exit).length;

  return {
    trend: { enter: trendEnter, exit: trendExit },
    pullback: { enter: pullbackEnter, exit: pullbackExit },
    breakout: { enter: breakoutEnter, exit: breakoutExit },
    squeeze: { enter: squeezeEnter, exit: squeezeExit },
    momentum: { enter: momentumEnter, exit: momentumExit },
    supertrend: { enter: superEnter, exit: superExit },
    reversion: { enter: reversionEnter, exit: reversionExit },
    stochastic: { enter: stochasticEnter, exit: stochasticExit },
    confluence: { enter: bulls >= params.votes, exit: bears >= params.votes },
  };
}

export function agreement(row: RawFrame, prev: RawFrame | undefined, params: Params, volMean: number | null): string[] {
  const set = evaluateBar(row, prev, params, volMean);
  return (["trend", "pullback", "breakout", "momentum", "supertrend"] as StrategyName[]).filter((name) => set[name].enter);
}

export function prepare(bars: Bar[], strategy: StrategyName, params: Params, atrPeriod: number): Frame[] {
  const rows = enrich(bars, params, atrPeriod);
  const volMean = rollShift(
    bars.map((b) => b.volume),
    params.channel,
    (w) => w.reduce((a, b) => a + b, 0) / w.length,
  );
  return rows.map((row, i) => {
    const side = evaluateBar(row, i > 0 ? rows[i - 1] : undefined, params, volMean[i]);
    return { ...row, enter: side[strategy].enter, exit: side[strategy].exit };
  });
}
