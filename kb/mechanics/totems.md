---
title: Totems
status: done
tracker_topic: "Totems"
tracker_note: "done (0.5.x; recheck 1.0)"
defaults: v=0.5.5.9
---

Version: game data 0.5.5.9 + 0.5.x (researched 2026-11-17). Re-check at 1.0.

## What totems are
@ v=0.5.5.9 vol=stable conf=confirmed date=2026-11-17
Totems are allied structures that use skills for you. They are not minions: their skills use your stats (so minion modifiers don't help them), but they have their own defences and can be killed.

- src: RePoE poe2 keywords.json "Totems" [S002], tier 2; poe2wiki Ballista [S604], tier 2; retrieved 2026-11-17

## Limit
@ v=0.5.x vol=may-change conf=confirmed date=2026-11-17
Base totem limit is 1, shared across all totem types by default. Some skills have a higher own limit (e.g. Spell Totem base 2, Shockwave Totem 1). Raised by supports, gear and passives; poe2wiki says the attack-totem max is 5. The Ancestral Bond keystone removes the limit but makes each totem reserve spirit.
- src: poe2wiki Ballista [S604], poe2wiki Totem [S639], tier 2; Mobalytics Limit [S076], tier 3; game keywords "Totems" (shared limit), tier 2; retrieved 2026-11-17
- conf: confirmed (base 1, shared); single-source (max 5, per-skill limits)
- notes: Ancestral Bond spirit cost — a player forum post says 75 per totem (tier 5, unverified).


## Embankment auras
@ v=0.5.5.9 vol=may-change conf=single-source date=2026-11-17
Totems with Embankment Auras buff players in range by totem type: Artillery Ballista +20% skill speed; Siege Ballista 25% more damage vs immobilised; Mortar Cannon 25% damage gained as fire; Shockwave Totem +30% AoE; Ancestral Warrior Totem +40% glory generation; Dark Effigy +40% DoT; Spell Totem +50% crit chance.
- src: game keywords "Embankment Auras", tier 2, retrieved 2026-11-17
- conf: single-source (game data)
- notes: which ascendancy/passive grants Embankment Auras not stated — find in ascendancies.json.


## Ballistas
@ v=0.5.5.9 vol=? conf=? date=2026-11-17 fill=v missing=vol,conf
Ballista totems use projectile attacks.
- src: game keywords "Ballista Totems", tier 2. single-source.
