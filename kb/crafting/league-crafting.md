---
title: League crafting: Verisium, Runeforging, Alloys (Runes of Aldur, 0.5)
status: done
tracker_topic: "Verisium & other league crafting"
tracker_note: "done (0.5 Runes of Aldur; 1.0 Reforging announced — see strategy/official-1.0-reveal)"
---

Scope: crafting added with the 0.5 Runes of Aldur league and how it's unlocked. Whether it stays in 1.0 is unknown — check at the 1.0 refresh. Expedition encounters → [[expedition]]. Augments → [[sockets-augments]].

## Remnants and Verisium
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-17
Ezomyte/Verisium Remnants appear in zones. Each starts with one inscribed rune; inscribing more runes picks a reward recipe, and each extra runeshape adds waves of Verisium-empowered monsters to fight before you get the reward. Monsters raised by Remnants (and Expedition bosses) drop Verisium, the crafting metal.
- src: RePoE poe2 keywords.json "Verisium Remnant", tier 2 (game data); poe2wiki Runes of Aldur [S722], tier 2; PoE2DB 0.5.0 notes copy [S115], tier 2; retrieved 2026-11-17
- vol: may-change (league mechanic)
- notes: Liquid Verisium instantly starts a Runic Remnant encounter with a random inscription ([[currency-index]]). In endgame, Expedition Remnants became these Remnants in 0.5 (PoE2DB notes).


## Verisium Runeforging (Verisium Anvil)
@ v=0.5.0 vol=may-change conf=confirmed date=2026-11-17
Unlocked in Act 1 via the Runeseeker quest. Spend Verisium to add Runic Ward to armour. Armour below level 55 gains Runic Ward with no downside; armour above level 55 trades some base defences for Runic Ward.
- src: PoE2DB Runeforging [S114], PoE2DB Runeforging (KR) [S117], tier 2; Mobalytics Runes of Aldur [S085], tier 3; retrieved 2026-11-17
- v: 0.5.0+
- notes: Runic Ward = last defence layer; absorbs damage that would take life below 1; regenerates 5%/s base, independent of life (Mobalytics Runic Ward guide, tier 3; keyword text). → [[energy-shield]] doc lists Runic Ward basics. For a levelling character, free Runic Ward on sub-55 armour is a cheap survivability layer [INFERRED].


## Unlock schedule (campaign)
@ v=0.5.0 vol=may-change conf=single-source date=2026-11-17
Act 1 — Verisium Anvil, Runeforged armours. Act 2 (Farrow's quest) — Runic Inscriptions unlock Alloys. Act 3 — Unique Runeforging for unique weapons and armour. Act 4 — Ancient Runes. Expedition — Kalguuran unique weapon/armour/jewellery recipes.
- src: PoE2DB Runeforging notes [S116], tier 2; Kami-labs 0.5.0 notes copy [S026], tier 5; retrieved 2026-11-17
- vol: may-change (1.0 campaign restructure)
- conf: single-source (tier 2)
- notes: Skip-route impact: these are side quests — decide which to take. → strategy/skip-route.


## Alloys
@ v=0.5.0 vol=may-change conf=confirmed date=2026-11-17
13 Alloy currencies (Runic, Adaptive, Expansive, Protective, Swift, Cyclonic, Prismatic, Mystic, Sovereign, Celestial, Transcendent, The Runebinder's, The Runefather's). Each removes a random mod from a rare and adds a guaranteed crafted mod — like a Perfect Essence. Drop levels in data: 13, 23, 45, 65.
- src: RePoE base_items.json (`CurrencyVerisiumAlloy*`), tier 2; PoE2DB 0.5.0 notes [S597], tier 2; retrieved 2026-11-17
- v: 0.5.0+
- notes: Counts as the item's one crafted mod ([[approach]]). Specific mod per alloy not captured yet.


## Unique Runeforging and Starlit Ores
@ v=0.5.0 vol=may-change conf=confirmed date=2026-11-17
From Act 3, unique weapons and armour that drop below level 55 can have their base upgraded (more damage, or more defence plus Runic Ward). Uniques above 55 can still be runeforged for Runic Ward at the cost of other defences. Starlit Ores (e.g. Revered Starlit Ore, dropped by The Aberration) forge new uniques at the anvil; Crests (Medved's, Vorana's, Uhtred's, Olroth's) transform unique items.
- src: PoE2DB Runeforging [S117], PoE2DB notes [S121], tier 2; poe2wiki Runes of Aldur [S722] and Navbox [S726], tier 2; retrieved 2026-11-17
- v: 0.5.0+
- notes: Makes low-level uniques endgame-viable — affects which cheap uniques are worth buying; check in economy batch.


## Other 0.5 Remnant crafts
@ v=0.5.0 vol=may-change conf=single-source date=2026-11-17
Remnants also craft Fluxes (3, which change the resistance types on an item from one element to another; Thaumaturgic Flux levels Kalguuran skill gems), Meta crafting runes (15), Mythical early-game runes (13, for level 15+ characters), Kalguuran skills and supports (cost Runic Ward, no colour, no attribute/weapon requirement).
- src: PoE2DB 0.5.0 notes [S119], tier 2; Kami-labs 0.5.0 notes copy [S028], tier 5; poe2wiki Runes of Aldur [S722], tier 2; retrieved 2026-11-17
- conf: single-source (tier 2)
- notes: Mythical early runes are a levelling power spike if Remnants stay in 1.0. [INFERRED]
