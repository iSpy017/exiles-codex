---
title: Flasks
status: done
tracker_topic: "Flasks"
tracker_note: "done (0.5.x; recheck 1.0)"
defaults: v=0.5.5.9
---

Version: game data 0.5.5.9 + 0.5.x sources (researched 2026-11-17). Re-check at 1.0.
"Game keywords" = [RePoE poe2 keywords.json](https://github.com/repoe-fork/poe2), tier 2.

## Slots and types
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-17
Two flask slots by default: one life flask, one mana flask (more only if something says so). Flasks recover over their duration by default, not instantly.
- src: poe2wiki Flask [S616], tier 2; Mobalytics Flasks [S067], tier 3; retrieved 2026-11-17
- notes: game keywords also define "Utility Flasks" (timed buffs) — [INFERRED] legacy/unused in 0.5.x since both tier-2/3 sources say only life + mana slots; verify in base_items.json.


## Recovery wasted at full
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-17
By default a flask's effect ends when you reach full unreserved life/mana — leftover recovery is lost. Some uniques override this.

- src: Mobalytics Flasks [S067], tier 3; poe2wiki Life flask [S698] (unique with "Effect is not removed when Unreserved Life is Filled"), tier 2; retrieved 2026-11-17

## Charges
@ v=0.5.5.9 vol=may-change conf=confirmed date=2026-11-17
Flasks use charges; kills refill them: Normal = ½ monster Power, Magic = Power, Rare/Unique = 2× Power. Checkpoints and wells fully refill. Flasks only hold charges while equipped (unequipping empties them).

- src: game keywords "Flasks", tier 2; poe2wiki Flask [S616], tier 2; retrieved 2026-11-17

## Example bases (life)
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-17 fill=vol
- Greater 150 life / 4 s · Grand 260 / 5 s · Giant 340 / 4 s · Colossal 450 / 4 s; each 10 charges per use, 70–75 max.
- src: poe2wiki List of life flasks [S701], tier 2; Mobalytics Flasks [S067] (Colossal 10/75), tier 3; retrieved 2026-11-17
- conf: confirmed (Colossal); single-source others
- notes: full base list → [[items/bases-implicits]] from base_items.json.


## Charge generation / instant recovery on belts and uniques
@ v=0.5.x vol=may-change conf=single-source date=2026-11-17 fill=vol
- Examples: belts with "Flasks gain X charges per second" (e.g. Fine Belt implicit 0.17/s), "Life Flasks used while on Low Life apply Recovery Instantly", "Life Recovery from Flasks also applies to Energy Shield", Overflowing Chalice buff (+2 charges/s, 30% increased recovery).
- src: poe2wiki Fine Belt [S695], poe2wiki List of unique belts [S702], tier 2; game keywords "Overflowing Chalice"; retrieved 2026-11-17
- conf: single-source each
- notes: Vaal Pact blocks life flask use (Mobalytics). Monster mod "Siphons Flask Charges" removes 3 flask + charm charges every 3 s within 3.6 m (game keywords).
