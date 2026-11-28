# Exile's Codex — Exchange margin page (#ce)

- Live: https://ispy017.github.io/exiles-codex/#ce (nav "Exchange margin"). Code: `app/exchange.js` (`window.CE`, pure functions exported for node), tests `tools/test_exchange.js` (run in the deploy, failures block it). Built 2026-11-28.
- Input: pair names, Available and Competing rows (paste `22 : 1 12,187`, `< 3.05 : 1 139`, `1 : 3 20`, `22 12187`; rows stay editable; unparseable lines are listed and ignored).
- Output: best Available (highest R) / best Competing (lowest R) with price per unit (1/R), spread, midpoint, liquidity label, first-in-line buy order (this pair, `bestComp − tick`) and sell order (reverse pair, written `1 : (bestAvail + tick)`), round-trip margin `buyR / sellR − 1`, profit for a stake, margin × fills/hour, instant-fill depth both ways. "No room to flip" when the best orders are within two ticks.
- Cross-currency check: price in A, price in B, A per 1 B → gain both ways, before fees (KB example 140 ex / 6.25 chaos / 28 ex per chaos = +25% on cost).
- Watchlist: per-device `localStorage` key `codex-ce`, ranked by margin × fills/hour (typed by David until volume data exists); "copy as CSV" gives rows in the `data/prices/*_exchange-books.csv` format.
- Rules it encodes: [[strategy/flipping-strats]] (undercut by the smallest step; margin × volume). Mechanics: [[economy/currency-exchange]].
- Assumptions, all editable on the page and constants at the top of `exchange.js`: tick 0.01 [INFERRED from two-decimal ratios + creator's ".01"]; Competing "Stock" counted in X (unconfirmed, toggle); spread < 5% tight, 5–50% thin, > 50% illiquid (David's provisional thresholds). Gold order fee left out on purpose: gold only costs time.
- Aggregated `<`/`>` rows count in depth at their bound ratio (flagged approximate) and are never used as best.
- Out of scope so far: screenshot OCR, exchange-history volume, poe.ninja.
