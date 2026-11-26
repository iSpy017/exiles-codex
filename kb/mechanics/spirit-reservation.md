---
title: Spirit & Reservation
status: done
tracker_topic: "Spirit & reservation"
tracker_note: "done (0.5.x; campaign spirit needs 1.0 check)"
defaults: v=0.5.5.9
---

Version: game data 0.5.5.9 + 0.5.x sources (researched 2026-11-17). Re-check at 1.0 (campaign changes may move the spirit quests).

## What spirit is
@ v=0.5.5.9 vol=may-change conf=confirmed date=2026-11-17
Spirit is a pool used to switch on and keep up persistent effects (persistent buffs/auras, heralds, permanent minions, meta gems). Persistent skills are toggled in the Skills Panel. Reserving doesn't lower your maximum — it locks part of it.

- src: game keywords "Spirit", "Reservation", "Persistent Skills", "Minions", tier 2 (RePoE [S002]); Mobalytics Spirit [S088], tier 3; retrieved 2026-11-17

## Spirit can differ per weapon set
@ v=0.5.5.9 vol=may-change conf=confirmed date=2026-11-17
Each weapon set can have a different spirit total (e.g. a sceptre in one set, set-specific passives, set-specific persistent skills). If a swap drops your spirit, some reservations may not fit.
- src: game keywords "Spirit", "Weapon Sets", tier 2; Maxroll Spirit guide [S037], tier 3; retrieved 2026-11-17
- notes: Maxroll advises testing swaps somewhere safe before bosses.


## Campaign spirit: 100 total
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-17
The campaign gives 100 max spirit in total from three boss/quest rewards (skull items you consume). Still 100 after Cruel difficulty was removed (0.3).
- src: Mobalytics Spirit [S088], tier 3; Poe-Vault "Does the campaign still grant 100 spirit" (2025-09-10), tier 3; poe2wiki Spirit [S636] (quest items grant spirit), tier 2; retrieved 2026-11-17
- vol: may-change — needs-1.0-check (new acts, Interludes removed)
- conf: confirmed (100 total)
- notes: exact bosses/amounts per boss → [[campaign/permanent-rewards]]. A source names Act 1's King in the Mists → +30 (tier 5, verify).


## Gear spirit
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-17
Sceptres have a 100-spirit implicit, and explicit mods can push a sceptre past 200. Amulets and body armours can roll spirit as explicits; the Solar Amulet base has a 10–15 spirit implicit. Some uniques give spirit (e.g. Enfolding Dawn +100).
- src: Mobalytics Spirit [S088], tier 3; poe2wiki Spirit [S636], tier 2; PoE2DB Spirit [S111] (unique examples), tier 2; retrieved 2026-11-17
- conf: confirmed (sceptre 100, amulet/body explicits); single-source (Solar Amulet range, roll ranges)
- notes: exact roll tiers → mods.json in the items batch.


## Free (non-reserving) persistents
@ v=0.5.x vol=may-change conf=single-source date=2026-11-17
Persistent buffs and permanent minions granted by item implicits (e.g. sceptres) or by ascendancy passives don't reserve spirit.

- src: poe2wiki Spirit [S636], tier 2, retrieved 2026-11-17

## Reservation efficiency
@ v=0.5.x vol=? conf=single-source date=2026-11-17 missing=vol
"Spirit Reservation Efficiency" mods reduce what skills reserve; some are conditional (e.g. per 100 max life for buff skills).
- src: PoE2DB Spirit [S111], tier 2, retrieved 2026-11-17
- notes: link to the user's spirit-gem price lesson in [[strategy/league-lifecycle-pricing]].
