# Expected cost of common crafts

Status: partial. Currency prices filled from [[price-snapshot-2026-11-17]] (poe.ninja, Forbidden Rites, late league). Omen, essence and bone prices still missing (other poe.ninja tabs). All prices volatile — redo at 1.0 league start.

## How to estimate a craft's cost
- Claim: Expected cost = sum of deterministic steps (fixed cost) + gamble steps × expected attempts. For a gamble step with success chance p per attempt, expected attempts = 1/p, so expected cost = cost per attempt ÷ p. Add the replacement cost of anything a failure destroys or bricks.
- Version: n/a (arithmetic)
- Volatility: stable
- Source: standard expected-value arithmetic — [INFERRED]: no game source needed; the p values must come from game data (mod weights) or a craft-of-exile-style tool
- Confidence: [INFERRED]
- Notes: Mod weights live in RePoE mods.json `spawn_weights` (tier 2) — p for "Exalt hits mod X" = weight(X) ÷ sum of weights of all mods that can still roll on that item. Can be scripted later if a specific craft matters.

## Unit costs per step (Forbidden Rites, 2026-11-17)
- Claim (1 div ≈ 528 ex ≈ 11 chaos):
  - Exalted ≈ 0.002 div · Greater Exalted ≈ 25 ex (0.05 div) · Perfect Exalted 2.6 div
  - Chaos ≈ 0.09 div · Greater Chaos ≈ 0.27 div · Perfect Chaos 9.7 div
  - Orb of Annulment ≈ 0.32 div · Fracturing Orb 8.5 div · Hinekora's Lock 1,800 div
  - Regal ≈ 3 ex · Orb of Alchemy ≈ 4 ex · Vaal Orb ≈ 8 ex · Artificer's Orb ≈ 27 ex
  - Perfect Jeweller's ≈ 0.36 div · Greater Jeweller's ≈ 9 ex
  - Architect's Orb 11 div (50% destroy → expected cost of one successful double-corrupt ≈ 22 div + the item's value × 1 lost item on average)
- Version: 0.5.5 (Forbidden Rites)
- Volatility: volatile
- Source: poe.ninja Currency, Forbidden Rites, 2026-11-17 (David's saved page), tier 4
- Confidence: single-source
- Notes: Architect's arithmetic uses the 50/50 from [[corruption]] [INFERRED from that rate].

## Reference craft costs (incomplete)
- Claim:
  - Perfect-Exalt slam on a 5-mod rare: 2.6 div per attempt; with p = chance the new mod is one you want, expected ≈ 2.6 ÷ p div. E.g. p = 0.25 → ≈10 div.
  - Fracture + chaos-spam jewel: 8.5 div (fracture, only lands on a random mod — p ≈ 1/4 to fracture the wanted mod on a 4-mod jewel → ≈34 div expected before chaos spam) + Chaos at 0.09 div each ÷ p(hit).
  - Annul-and-retry steps: 0.32 div per annul; Greater Annulment / Sinistral/Dextral omens not priced yet.
- Version: 0.5.5
- Volatility: volatile
- Source: prices above (tier 4) + EV arithmetic [INFERRED]
- Confidence: [INFERRED] — the p values are placeholders, not computed from mod weights
- Notes: Still to price: omens (Light, Sinistral/Dextral Exaltation/Erasure/Annulment, Whittling, Abyssal Echoes, Crystallisation), Perfect essences, Preserved/Ancient bones. Ask David for the poe.ninja Omens / Essences / Abyss tabs, or spot-check via the GGG exchange API ([[price-sites]]).

## Rough guide figures (not prices — orders of magnitude)
- Claim: Guide example: an expensive deterministic high-end staff craft ~200 div vs a gamble version ~30–40 div; one 0.5 guide estimates gamble crafts cost 2–5× the price of buying the same finished item.
- Version: 0.5.x
- Volatility: volatile
- Source: ameblo.jp blog and Timesaver blog, tier 5 (RMT-linked; leads only, unverified), retrieved 2026-11-17
- Confidence: [INFERRED] — unverified, do not use for decisions
