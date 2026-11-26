---
title: Weapon Sets & Weapon Swap
status: done
tracker_topic: "Weapon swap / weapon sets"
tracker_note: "done (0.5.x; points need 1.0 check)"
defaults: v=0.5.5.9
---

Version: game data 0.5.5.9 + 0.5.x (researched 2026-11-17). Re-check at 1.0.
"Game keywords" = [RePoE poe2 keywords.json](https://github.com/repoe-fork/poe2), tier 2.

## Two weapon sets, auto-swap per skill
@ v=0.5.5.9 vol=may-change conf=confirmed date=2026-11-17
Characters have two weapon sets. Skills use the active set if they can, otherwise auto-swap to the other; you can pin a set per skill in its info panel. Manual swap key is X by default; swapping has a short fixed cooldown.

- src: game keywords "Weapon Sets", tier 2; poe2wiki Weapon set [S642], tier 2; retrieved 2026-11-17

## Weapon set passive points
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-17
Weapon set points let you allocate some of your existing passive points differently per set. They're not extra points — each converts one of your normal points (though the Book of Specialisation item also gives 2 normal points). Campaign total: 24, from Books of Specialisation (2 each, from bosses/quests, e.g. Act 1's optional boss The Crowbell) and bonus objectives; Olroth's Boon gives 1 more. Keystones and jewel sockets can't be set-specific. Points allocated in both sets need one removed from each to free one normal point.
- src: poe2wiki Weapon set [S642], poe2wiki Passive Tree Nodes [S711], poe2wiki Notable [S706], poe2wiki Passive Skill Points [S709], tier 2; Mobalytics Dual Specialisation [S064], tier 3; PoE2DB Weapon Set Passive Skill Points [S112], tier 2; retrieved 2026-11-17
- vol: may-change — needs-1.0-check (campaign changes)
- conf: confirmed (24, convert not extra)
- notes: Shapeshift skills get a third set (up to 24). Witchhunter's Weapon Master converts up to 100 points ([poe2wiki Weapon Master](https://www.poe2wiki.net/wiki/Weapon_Master)) — relevant to char 2 (Witchhunter loop). Older guides say ~16 points (early access) — superseded.


## Spirit per set
- Each set can have different spirit — see [[mechanics/spirit-reservation]].

## Things lost on swap
@ v=0.5.5.9 vol=may-change conf=? date=2026-11-17 fill=vol missing=conf,src
- Combo is lost on weapon swap and only builds with the weapon the combo skill is bound to (game keywords "Combo").
- Elemental Surges are tied to the current weapon and don't carry over (game keywords "Elemental Surges").

- v: 0.5.5.9, single-source (game data).

## Respec
- Refund passives at The Hooded One in town or Doryani (Act 3 / hideout) — [Mobalytics Dual Specialisation](https://mobalytics.gg/poe-2/guides/dual-specialisation), tier 3. Costs → [[classes/respec]].
