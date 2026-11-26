---
title: Minions
status: partial
tracker_topic: "Minions"
tracker_note: "partial (base life/damage scaling added — derived values [INFERRED]; Life vs Minion Life column unresolved; Bone Construct/Spectre stats missing)"
defaults: v=0.5.5.9
---

Status: partial — base life/damage scaling now covered (batch 39, derived values [INFERRED]); open: which Monster Stats column the game applies to player minions, Bone Construct / Spectre stats. Skill list and per-level spirit in [[gems/minion-skills]]; per-minion multipliers and derived values in [[gems/minion-stats]], [[gems/minion-stats]].
Version: game data 0.5.5.9 + 0.5.x (researched 2026-11-17; scaling added batch 17; spirit pattern batch 22; base stats batch 39). Re-check at 1.0.
"Game keywords" = [RePoE poe2 keywords.json](https://github.com/repoe-fork/poe2), tier 2.

## Types
@ v=0.5.5.9 vol=may-change conf=confirmed date=2026-11-17
Minions are summoned allies. Persistent minions reserve spirit while active. Reviving minions heal after avoiding damage for a while and revive after a short delay when killed; the delay resets whenever another reviving minion dies. Temporary minions never revive.
- src: game keywords "Minions", "Reviving Minions", "Temporary Minion", tier 2; poe2wiki Reviving Minions [S721], tier 2; retrieved 2026-11-17
- notes: [poe2wiki Minion](https://poe2wiki.net/wiki/Minion) gives the number: revive if no allied minion died in the past 7 s by default. PoE2DB gem pages show "minion base resummon time ms [12000]" on Skeletal Warrior and companion gems — [INFERRED] a 12 s base resummon; not reconciled with the 7 s figure.


## Companions
@ v=0.5.5.9 vol=may-change conf=confirmed date=2026-11-17 fill=vol
Companions are stronger reviving minions; by default only one companion of any type at a time (e.g. a Druid wolf pack counts as one).

- src: game keywords "Companions", tier 2; poe2wiki Reviving Minions [S721], tier 2; retrieved 2026-11-17

## Reforming / died vs killed / commands / offerings
@ v=0.5.5.9 vol=may-change conf=single-source date=2026-11-17 fill=vol
Dead persistent minions get a "Minion Reforming" timer and return when it ends. Minions that expire or are despawned "died" but weren't "killed" — kill-triggers only fire at 0 life. Command skills order one minion; Offering skills target a Skeleton to make a damageable Offering Spike with buffs.

- src: game keywords "Minion Reforming", "Minion Death and Killing Minions", "Minion Commands", "Offering Skills", tier 2, retrieved 2026-11-17
- conf: single-source (game data)

## Minion level vs gem level
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-26
Minion level = 2 × gem level (gem L1 → minion L2 … gem L40 → minion L80). Minion Mastery support gives +1 level to supported minion skills.
- src: poe2db:Minions, tier 2, retrieved 2026-11-17; every minion gem level table in the PoE2DB corpus (crawl 2026-11-23, checked 2026-11-26)
- conf: confirmed (same source family, many pages agree)
- notes: "very underleveled" minions get an energy-generation penalty with Cast on Minion Death (same page).


## Minion life/damage scale table (batch 39)
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
PoE2DB's Monster Stats table has "Minion Life" and "Minion Damage" columns per level (L2 83 / 4.42, L20 886 / 50.39, L40 2,490 / 204.04, L80 10,084 / 1,776.43). Each minion type multiplies them by its own Life % / Damage % (e.g. Skeletal Warrior 88% / 70%, Raised Zombie 70% / 75%, Raging Spirit 25% / 70%). PoE2DB's level-68 minion blocks match this multiplication on 3 pages.
- src: poe2db:Monster Monster Stats rows (Monster.txt lines 583, 601, 621, 661), tier 2, crawl 2026-11-23; minion blocks on gem pages
- conf: single-source for the table; multiplication verified at L68 only
- notes: [INFERRED] that "Minion Life" (not plain "Life") applies in game — PoE2DB doesn't state it. Minion Life exceeds monster Life below level 64 and is lower from 64. Basic-attack ranges follow the plain "Damage" column, so what "Minion Damage" feeds is unclear. Full tables → [[gems/minion-stats]], [[gems/minion-stats]]. Conflicts → [[conflicts]].


## Minion defences are per type
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
Armour/evasion/ES come from per-minion bonuses: Warrior +50% armour and 30% block, Brute +70% armour, Reaver +20% armour, Rhoa +50% armour and evasion, Wolf +30% evasion, Mist Raven +100% evasion; mage skeletons have ES = 10–15% of life (Demon Magus 50%).

- src: minion blocks at the bottom of the PoE2DB gem pages (see [[gems/minion-stats]]), tier 2, crawl 2026-11-23

## Minion resistances
@ v=0.5.x vol=may-change conf=inferred date=2026-11-23
Minion blocks show 0% on all four resistance cells for nearly all minions. The display shows 50% on one element for Skeletal Arsonist (fire), Frost Mage (cold), Storm Mage (lightning) and Infernal Hound (fire), while the PoB data block on the same pages lists 0. PoE2DB states no general minion default-resistance rule; its "Monster Default" table (75 max res, 75 phys DR cap, +30% crit damage) is for monsters and not said to apply to player minions.
- src: Skeletal_Frost_Mage.txt ~2216 vs ~2371 and the other gem pages; poe2db:Monster Monster Default section; tier 2, crawl 2026-11-23
- conf: [INFERRED] cell order fire/cold/lightning/chaos (PoB key order); display-vs-data conflict open
- notes: Carrion Call sets minion res equal to yours (next entry).


## Which player modifiers reach minions
@ v=0.5.x vol=may-change conf=single-source date=2026-11-17 fill=vol
There is no general inheritance rule. Minions use their own modifiers; effects pass through only where an item/passive/gem says so. Examples (PoE2DB): Carrion Call — minion res = yours, more minion max life; Loyalty / Romira's Requital — minions take part of your hit damage, lower max life; Tangmazu's Thurible — companion evasion/deflection based on yours; Chober Chaber / Trenchtimbre — minion damage / attack-speed mods also affect you; Umbilicus Immortalis — your life flask also applies to minions.

- src: poe2db:Minions, tier 2, retrieved 2026-11-17
- conf: single-source; "no general rule" is the page's own lack of an inheritance section — [INFERRED] absence, verify with a build

## Spirit
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23
Level-scaled persistent minion gems get cheaper as they level — e.g. Skeletal Warrior 60 → 22 → 20 spirit at gem 1 / 10 / 20 (first 2 minions free), Skeletal Frost Mage 120 → 43 → 39, Skeletal Brute 165 → 54 → 48. Flat-cost minion persistents: Raging Spirits and Ravenous Swarm 30, Wolf Pack and Sacrifice 60, Demon Magus and Rhoa Mount 100. Full table → [[gems/minion-skills]].
- src: PoE2DB gem pages (e.g. poe2db:Skeletal_Brute), tier 2, crawl 2026-11-23
- vol: may-change (1.0 support/minion changes)
- conf: single-source (game data); the level-table column is labelled "Mana" but matches the Reservation line → [INFERRED] spirit
- notes: Enormity (Hulking Minions) support raises spirit cost, no number. Reservation-efficiency mods exist on items (e.g. The Raven's Flock 30–50% increased). Skeletal Warrior can't be engraved since 0.2.0 (sceptre-granted). → [[mechanics/spirit-reservation]].


## Not yet sourced
- Which Monster Stats column (Life vs Minion Life) the game applies to player minions; Unearth Bone Construct, Spiraling Conspiracy and Offering Spike stats; Spectre stats and spirit by bound monster.
