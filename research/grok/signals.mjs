import { readFileSync } from "node:fs";
import { prepare } from "./indicators.ts";
import { DEFAULT_PARAMS } from "./profiles.ts";

// An isolated signal calculator. Position sizing and fills belong to the paper engine.
const { books, strategy, atrPeriod } = JSON.parse(readFileSync(0, "utf8"));
const signals = {};
for (const [symbol, bars] of Object.entries(books)) {
  const rows = prepare(bars, strategy, DEFAULT_PARAMS, atrPeriod);
  signals[symbol] = {
    enter: rows.map(row => row.enter),
    exit: rows.map(row => row.exit),
  };
}
process.stdout.write(JSON.stringify(signals));
