# Resistances & Caps

Version: game data 0.5.5.9 + 0.5.x sources (researched 2026-11-17). Re-check at 1.0 — campaign penalty WILL change (1.0 removes Interludes, adds Acts 5–6).
"Game keywords" = [RePoE poe2 keywords.json](https://github.com/repoe-fork/poe2), tier 2.

## What resistances do
- Claim: Fire, cold, lightning and chaos resistance each reduce damage of that type, up to a maximum. Fire/cold/lightning are the elemental resistances. Sources: gear, passives, quest rewards.
- Version: 0.5.5.9
- Volatility: stable
- Source: game keywords "Resistances", tier 2; [Mobalytics Resistances](https://mobalytics.gg/poe-2/guides/resistances), tier 3; retrieved 2026-11-17
- Confidence: confirmed
- Notes: e.g. 1000 fire damage at 75% fire res → 250 taken. Each point matters more near the cap: 60→70% cuts damage taken by a quarter (400→300 per 1000). Source: [poe2wiki Chaos resistance](https://www.poe2wiki.net/wiki/Chaos_resistance), tier 2.

## Caps
- Claim: Default maximum for elemental and chaos resistance is 75%. Maximum resistance can't go above 90%. "Uncapped" resistance (shown in brackets on the character panel) is your total before the cap; "overcapped" is the amount above your max.
- Version: 0.5.5.9
- Volatility: may-change
- Source: game keywords "Maximum Resistances", "Uncapped Resistance", "Overcapped Resistance", tier 2; [poe2wiki Maximum Resistances](https://www.poe2wiki.net/wiki/Maximum_Resistances), tier 2; retrieved 2026-11-17
- Confidence: confirmed

## Campaign penalty (0.5.x schedule)
- Claim: Elemental resistance drops by 10% around each act end up to Act 4, then by area level through the Interludes: −10% (Act 2), −20% (Act 3), −30% (Act 4), −40% (area level 54–59), −50% (60–64), −60% (65+, endgame). It's permanent and unavoidable.
- Version: 0.5.x
- Volatility: may-change — needs-1.0-check (Interludes removed in 1.0)
- Source: [poe2wiki Chaos Resistance](https://poe2wiki.net/wiki/Chaos_Resistance) (table), [poe2wiki Maximum Resistances](https://www.poe2wiki.net/wiki/Maximum_Resistances), tier 2; [Mobalytics Resistances](https://mobalytics.gg/poe-2/guides/resistances) (−10% per act), tier 3; GGG forum player answers (−60% endgame), tier 5; retrieved 2026-11-17
- Confidence: confirmed for −60% endgame total; single-source for the area-level breakpoints
- Notes: game keyword text only says elemental res "are lowered as you progress". Practical: endgame needs 135% uncapped per element to sit at 75% — [INFERRED] arithmetic. Campaign quests give some permanent resistance back → [[campaign/permanent-rewards]]. Does the penalty also hit chaos? The wiki table sits on the chaos page but wording says "elemental" — verify.

## Lowering enemy resistance
- Claim: Exposure, curses and other reductions can push enemy resistance negative (more damage taken). "Ignore resistance" treats it as 0%. "Resisted by other value" replaces the target's resistance with a fixed value that penetration can't touch. Penetration only works on hits and stops at 0%.
- Version: 0.5.5.9
- Volatility: may-change
- Source: game keywords "Exposure", "Ignoring Resistances", "Resisted by Other Value", "Resistance Penetration", tier 2; [Mobalytics Resistances](https://mobalytics.gg/poe-2/guides/resistances), tier 3; retrieved 2026-11-17
- Confidence: confirmed
- Notes: detail in [[mechanics/exposure-penetration]].

## Monster resistance mods
- Claim: "Fire/Cold/Lightning Resistant" monster mods give +50% to that resistance and +10% to its maximum; "Chaos Resistant" gives +50% chaos res; an "Elemental Resistance Aura" gives allies within 5 m +35% to all elemental res.
- Version: 0.5.5.9
- Volatility: may-change
- Source: game keywords (monster modifier entries), tier 2, retrieved 2026-11-17
- Confidence: single-source (game data)
