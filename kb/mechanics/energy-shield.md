---
title: Energy Shield (+ other damage buffers)
status: done
tracker_topic: "Energy shield"
tracker_note: "done (0.5.5.9; recheck 1.0)"
defaults: v=0.5.5.9
---

Version: game data 0.5.5.9 (researched 2026-11-17). Re-check at 1.0.
"Game keywords" = [RePoE poe2 keywords.json](https://github.com/repoe-fork/poe2), tier 2.

## What ES does
@ v=0.5.5.9 vol=stable conf=confirmed date=2026-11-17
Energy Shield takes damage before life. Chaos damage removes double its value from ES. Bleeding and Poison skip ES and hit life directly.

- src: game keywords "Energy Shield", tier 2; poe2db:Keywords (chaos double), tier 2; retrieved 2026-11-17

## Recharge
@ v=0.5.5.9 vol=may-change conf=single-source date=2026-11-17
Lost ES starts recharging after a 4 s delay, at 12.5% of max ES per second. Taking more ES damage resets the delay. "Recharge rate" mods speed the refill; "faster start of recharge" mods shorten the delay.
- src: game keywords "Energy Shield Recharge", "Energy Shield Recharge Rate", "Faster Start of Energy Shield Recharge", tier 2, retrieved 2026-11-17
- conf: single-source (game data)
- notes: Full refill from empty ≈ 4 s delay + 8 s = 12 s base — [INFERRED] arithmetic.


## Low ES
@ v=0.5.5.9 vol=? conf=single-source date=2026-11-17 missing=vol
"Low Energy Shield" = at or below 35% of max ES.

- src: game keywords "Low Energy Shield", tier 2, retrieved 2026-11-17
- conf: single-source (game data)

## ES leech
@ v=0.5.5.9 vol=may-change conf=single-source date=2026-11-17
ES leech recovers a % of hit damage over 1 s. Damage per hit counts up to 40,000 max. Monsters' leech resistance grows with their level. Only one ES leech instance at a time; all ES leech stops when ES is full. Life-leech modifiers don't apply to it.
- src: game keywords "Energy Shield Leech", tier 2, retrieved 2026-11-17
- conf: single-source (game data)
- notes: life leech → [[mechanics/recovery]] (batch 4).


## ES protecting mana
@ v=0.5.5.9 vol=? conf=single-source date=2026-11-17 missing=vol
Under "Energy Shield Protecting Mana" (keystone-style effect), ES only absorbs damage that would hit mana.

- src: game keywords, tier 2, retrieved 2026-11-17
- conf: single-source (game data)

## Life Recharge (special)
@ v=0.5.5.9 vol=? conf=inferred date=2026-11-17 missing=vol
A "Life Recharge" keyword exists: lost life recharges like ES (12.5%/s after 4 s) and ES recharge-rate/start modifiers apply to it.

- src: game keywords "Life Recharge", tier 2, retrieved 2026-11-17
- conf: [INFERRED] that this only applies when an effect grants it (it isn't a default player mechanic) — verify which keystone/ascendancy grants it.

## Other damage buffers
@ v=0.5.5.9 vol=may-change conf=? date=2026-11-17 missing=conf,src
- Guard: a buff that absorbs hit damage before life/ES. One Guard at a time; a new one keeps the larger and refreshes duration proportionally. Max Guard = 200% of max life. (game keywords "Guard", single-source)
- Runic Ward: last-line buffer. When damage would take life to 0, you drop to 1 life and ward soaks the rest; you still die if ward runs out. Regenerates 5%/s by default. Doesn't stop non-damage life loss. Monsters with ward can't be culled. Low ward = ≤35%. (game keywords "Runic Ward", "Low Runic Ward", single-source)
- v: 0.5.5.9, volatility may-change.
