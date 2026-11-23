# Life, Mana & Recovery (leech, recoup, regen)

Version: game data 0.5.5.9 (researched 2026-11-17). Re-check at 1.0.
"Game keywords" = [RePoE poe2 keywords.json](https://github.com/repoe-fork/poe2), tier 2. Same text is on [PoE2DB Keywords](https://poe2db.tw/us/Keywords) — counted as one source.

## Leech
- Claim: Leech recovers life, mana, ES or rage over 1 s, based on a % of hit damage dealt. Only one leech instance per resource recovers at a time, and all leech of that resource stops when it's full. Each hit counts as at most 40,000 damage. Monsters have leech resistance that rises with their level, cutting what you get.
- Version: 0.5.5.9
- Volatility: may-change
- Source: game keywords "Leech", "Life Leech", "Mana Leech", "Energy Shield Leech", "Rage Leech", tier 2, retrieved 2026-11-17
- Confidence: single-source (game data)
- Notes: Hits only — DoT doesn't leech ([INFERRED] from "when you deal damage with a Hit"). One-instance rule = leech is a top-up, not burst healing. Life-leech mods don't affect ES leech.

## Recoup
- Claim: Recoup returns a % of hit damage you took, over 8 s, to the stated resource.
- Version: 0.5.5.9
- Volatility: may-change
- Source: game keywords "Recoup", tier 2, retrieved 2026-11-17
- Confidence: single-source (game data)

## Regeneration
- Claim: Regen sources found so far: Consecrated Ground (5% max life/s, curses 50% less effective on you), Arcane Surge (20% more mana regen + 15% increased cast speed, 4 s). Zealot's Oath turns excess life regen into ES but stops ES recharge. Abyssal Wasting halves life regen for 6 s.
- Version: 0.5.5.9
- Volatility: may-change
- Source: game keywords "Consecrated Ground", "Arcane Surge", "Zealot's Oath", "Abyssal Wasting", tier 2, retrieved 2026-11-17
- Confidence: single-source (game data)
- Notes: base player life/mana regen values not yet sourced.

## Thresholds and special cases
- Low Life / Low Mana / Low ES = at or below 35% of max. (game keywords)
- Overflow: recovery that can overflow goes up to 1.5× your max. (game keywords "Overflow")
- Life Loss is not damage: ES and mitigation don't stop it, and it can kill. (game keywords "Life Loss")
- Life Recharge: some effects let life recharge like ES (12.5%/s after 4 s); granted by items such as a unique with "Life Recharges" ([poe2wiki Low Life](https://poe2wiki.net/wiki/Low_Life)). Not default. (game keywords "Life Recharge")
- "Take mana costs as damage": upfront costs hit you as a hit; per-second costs become DoT. (game keywords)
- Version: 0.5.5.9, volatility may-change, confidence single-source each.

## Rage (resource)
- Claim: Rage gives 1% more attack damage per point. Default max 30; you lose 1 every 0.2 s, paused for 4 s after gaining rage or taking damage. Only one hit per 0.5 s can grant rage.
- Version: 0.5.5.9
- Volatility: may-change
- Source: game keywords "Rage", tier 2, retrieved 2026-11-17
- Confidence: single-source (game data)

## Checkpoints & wells
- Claim: Reaching a checkpoint refills life, mana, flasks and charms; town wells refill flasks and restore life and mana. Waypoints count as checkpoints for revival.
- Version: 0.5.5.9
- Source: game keywords "Checkpoints", "Wells", tier 2, retrieved 2026-11-17
- Confidence: single-source (game data)
- Notes: relevant to the skip route — free full refill at every checkpoint.
