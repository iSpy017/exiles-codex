# Totems

Version: game data 0.5.5.9 + 0.5.x (researched 2026-11-17). Re-check at 1.0.

## What totems are
- Claim: Totems are allied structures that use skills for you. They are not minions: their skills use your stats (so minion modifiers don't help them), but they have their own defences and can be killed.
- Version: 0.5.5.9
- Volatility: stable
- Source: [RePoE poe2 keywords.json "Totems"](https://github.com/repoe-fork/poe2), tier 2; [poe2wiki Ballista](https://poe2wiki.net/wiki/Ballista), tier 2; retrieved 2026-11-17
- Confidence: confirmed

## Limit
- Claim: Base totem limit is 1, shared across all totem types by default. Some skills have a higher own limit (e.g. Spell Totem base 2, Shockwave Totem 1). Raised by supports, gear and passives; poe2wiki says the attack-totem max is 5. The Ancestral Bond keystone removes the limit but makes each totem reserve spirit.
- Version: 0.5.x
- Volatility: may-change
- Source: [poe2wiki Ballista](https://poe2wiki.net/wiki/Ballista), [poe2wiki Totem](https://poe2wiki.net/wiki/Totem), tier 2; [Mobalytics Limit](https://mobalytics.gg/poe-2/guides/limit), tier 3; game keywords "Totems" (shared limit), tier 2; retrieved 2026-11-17
- Confidence: confirmed (base 1, shared); single-source (max 5, per-skill limits)
- Notes: Ancestral Bond spirit cost — a player forum post says 75 per totem (tier 5, unverified).

## Embankment auras
- Claim: Totems with Embankment Auras buff players in range by totem type: Artillery Ballista +20% skill speed; Siege Ballista 25% more damage vs immobilised; Mortar Cannon 25% damage gained as fire; Shockwave Totem +30% AoE; Ancestral Warrior Totem +40% glory generation; Dark Effigy +40% DoT; Spell Totem +50% crit chance.
- Version: 0.5.5.9
- Volatility: may-change
- Source: game keywords "Embankment Auras", tier 2, retrieved 2026-11-17
- Confidence: single-source (game data)
- Notes: which ascendancy/passive grants Embankment Auras not stated — find in ascendancies.json.

## Ballistas
- Claim: Ballista totems use projectile attacks.
- Source: game keywords "Ballista Totems", tier 2. single-source.
