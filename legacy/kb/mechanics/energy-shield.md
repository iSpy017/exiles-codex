# Energy Shield (+ other damage buffers)

Version: game data 0.5.5.9 (researched 2026-11-17). Re-check at 1.0.
"Game keywords" = [RePoE poe2 keywords.json](https://github.com/repoe-fork/poe2), tier 2.

## What ES does
- Claim: Energy Shield takes damage before life. Chaos damage removes double its value from ES. Bleeding and Poison skip ES and hit life directly.
- Version: 0.5.5.9
- Volatility: stable
- Source: game keywords "Energy Shield", tier 2; [PoE2DB Keywords](https://poe2db.tw/us/Keywords) (chaos double), tier 2; retrieved 2026-11-17
- Confidence: confirmed

## Recharge
- Claim: Lost ES starts recharging after a 4 s delay, at 12.5% of max ES per second. Taking more ES damage resets the delay. "Recharge rate" mods speed the refill; "faster start of recharge" mods shorten the delay.
- Version: 0.5.5.9
- Volatility: may-change
- Source: game keywords "Energy Shield Recharge", "Energy Shield Recharge Rate", "Faster Start of Energy Shield Recharge", tier 2, retrieved 2026-11-17
- Confidence: single-source (game data)
- Notes: Full refill from empty ≈ 4 s delay + 8 s = 12 s base — [INFERRED] arithmetic.

## Low ES
- Claim: "Low Energy Shield" = at or below 35% of max ES.
- Version: 0.5.5.9
- Source: game keywords "Low Energy Shield", tier 2, retrieved 2026-11-17
- Confidence: single-source (game data)

## ES leech
- Claim: ES leech recovers a % of hit damage over 1 s. Damage per hit counts up to 40,000 max. Monsters' leech resistance grows with their level. Only one ES leech instance at a time; all ES leech stops when ES is full. Life-leech modifiers don't apply to it.
- Version: 0.5.5.9
- Volatility: may-change
- Source: game keywords "Energy Shield Leech", tier 2, retrieved 2026-11-17
- Confidence: single-source (game data)
- Notes: life leech → [[mechanics/recovery]] (batch 4).

## ES protecting mana
- Claim: Under "Energy Shield Protecting Mana" (keystone-style effect), ES only absorbs damage that would hit mana.
- Version: 0.5.5.9
- Source: game keywords, tier 2, retrieved 2026-11-17
- Confidence: single-source (game data)

## Life Recharge (special)
- Claim: A "Life Recharge" keyword exists: lost life recharges like ES (12.5%/s after 4 s) and ES recharge-rate/start modifiers apply to it.
- Version: 0.5.5.9
- Source: game keywords "Life Recharge", tier 2, retrieved 2026-11-17
- Confidence: [INFERRED] that this only applies when an effect grants it (it isn't a default player mechanic) — verify which keystone/ascendancy grants it.

## Other damage buffers
- Guard: a buff that absorbs hit damage before life/ES. One Guard at a time; a new one keeps the larger and refreshes duration proportionally. Max Guard = 200% of max life. (game keywords "Guard", single-source)
- Runic Ward: last-line buffer. When damage would take life to 0, you drop to 1 life and ward soaks the rest; you still die if ward runs out. Regenerates 5%/s by default. Doesn't stop non-damage life loss. Monsters with ward can't be culled. Low ward = ≤35%. (game keywords "Runic Ward", "Low Runic Ward", single-source)
- Version: 0.5.5.9, volatility may-change.
