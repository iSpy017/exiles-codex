# Shock and Electrocute
Status: partial. Have: shock numbers, electrocute duration/priming, list of skills and supports that electrocute. Missing: monster electrocute threshold value, buildup formula, shock magnitude scaling beyond the default.
Version: 0.5.x data (PoE2DB crawl 2026-11-23). Re-check everything at 1.0. Merged with the earlier library doc (2026-11-17 entries kept under "Carried over").
Sources: PoE2DB Keywords, Electrocute, Electrocution and gem pages (tier 2).

## Shock
- Claim: Shock makes targets take 20% increased damage. Default duration 4 s on players, 8 s on non-players. Lightning damage from hits contributes to shock chance: by default 1% chance per 4% of the target's Ailment Threshold dealt.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Keywords](https://poe2db.tw/us/Keywords), [PoE2DB Shock](https://poe2db.tw/us/Shock), tier 2, crawl 2026-11-23
- Confidence: confirmed
- Notes: Shocked buff has a "damage taken from shock" stat ([PoE2DB Shocked](https://poe2db.tw/us/Shocked)). Skills with an Electrocute Support cannot shock.

## Electrocute: what it does
- Claim: Electrocution stops the target performing any action; default duration 5 s. Only lightning damage from hits with specific skills or effects builds it; other lightning does not.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Electrocution](https://poe2db.tw/us/Electrocution), [PoE2DB Keywords](https://poe2db.tw/us/Keywords), tier 2, crawl 2026-11-23
- Confidence: confirmed
- Notes: Electrocuted targets count as Immobilised (Keywords). Liquid Emotions (Delirium instilling) result "Electrocution" (Paranoia, Suffering, Greed): enemies you electrocute take 20% increased damage ([PoE2DB Electrocution](https://poe2db.tw/us/Electrocution)).

## Electrocute threshold and priming
- Claim: Electrocute Threshold sets how much buildup is needed. Primed for Electrocution: Normal 40%, Magic 50%, Rare 60%, Unique 70% buildup. Higher Elemental Ailment Threshold lowers electrocute buildup received (player default threshold = half Life).
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Keywords](https://poe2db.tw/us/Keywords), [PoE2DB Electrocute Threshold](https://poe2db.tw/us/Electrocute_Threshold), tier 2, crawl 2026-11-23
- Confidence: single-source
- Notes: not found: any monster electrocute threshold number. Monster tables have none. Valako's Charge lists a raw stat "electrocute threshold +% final [100]" (meaning unclear, likely relates to the skill's targets) in [PoE2DB Valako's Charge](https://poe2db.tw/us/Valakos_Charge). History: 0.1.0e electrocute 25% harder to build; 0.2.0 about 44% slower on non-players.

## Skills that Electrocute (0.5.x)
- Claim: Skill gems that build electrocution: Enervating Nova (100-157% more buildup, ring 1 m to 2.6 m, buildup window 4 s), Conductive Runes (50% more buildup, 10 runes, limit 20), Voltaic Barrier (300% more buildup, cannot shock), Voltaic Grenade (150-340% more buildup, debuff 6 s, detonation 2.5 s), Valako's Charge (chain lightning, contributes, cannot shock), Electrocuting Arrow (attached rod makes all incoming lightning build electrocution; rod lasts until next electrocute; arrow duration 25 s), Voltaic Mark (marked enemy electrocutes when hit while primed; +25-35% increased buildup against marked; mark 8 s, buff 10 s granting 30% of damage as lightning).
- Version: 0.5.x
- Volatility: may-change
- Source: PoE2DB pages [Enervating Nova](https://poe2db.tw/us/Enervating_Nova), [Conductive Runes](https://poe2db.tw/us/Conductive_Runes), [Voltaic Barrier](https://poe2db.tw/us/Voltaic_Barrier), [Voltaic Grenade](https://poe2db.tw/us/Voltaic_Grenade), [Valako's Charge](https://poe2db.tw/us/Valakos_Charge), [Electrocuting Arrow](https://poe2db.tw/us/Electrocuting_Arrow), [Voltaic Mark](https://poe2db.tw/us/Voltaic_Mark), tier 2, crawl 2026-11-23
- Confidence: single-source each
- Notes: Electrocution Trap page exists (100% more buildup, cannot shock) but looks like a legacy/odd entry (level 13, tier 9); unverified for live drop. List built by corpus search of skill-gem descriptions; a skill with only a rule in its hidden stats could be missed.

## Supports and sources that Electrocute
- Claim: Electrocute Support (tier 2, +5 Dex): lightning damage can electrocute, supported skills cannot shock. Neural Overload (tier 3): nearby primed enemies are marked, hitting a marked enemy electrocutes. Eonyr's Thunder (lineage, level 65): same as Electrocute Support plus Voltaic Fulmination on killing electrocuted enemies. Items: Brain Rattler (all damage causes electrocution buildup), Kitoko's Current gloves (lightning hits contribute), Beyond Reach quiver (chaos hits also contribute to freeze and electrocute buildup).
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Electrocute](https://poe2db.tw/us/Electrocute), [PoE2DB Neural Overload](https://poe2db.tw/us/Neural_Overload), [PoE2DB Eonyr's Thunder](https://poe2db.tw/us/Eonyrs_Thunder), [PoE2DB Electrocution](https://poe2db.tw/us/Electrocution), tier 2, crawl 2026-11-23
- Confidence: single-source each
- Notes: the "Skill Gems" table on the Electrocute Support page (Lightning Arrow, Spark and others) is a recommended-support list, not a "can electrocute" list. Spark and Lightning Arrow recommend Electrocute at tier 2.

## Not electrocutable
- Claim: Skeletal Arsonist, Frost Mage, Reaver and Storm Mage minion skills carry flags that they cannot be electrocuted, frozen, or stunned.
- Version: 0.5.x
- Volatility: may-change
- Source: [Skeletal Frost Mage](https://poe2db.tw/us/Skeletal_Frost_Mage), [Skeletal Arsonist](https://poe2db.tw/us/Skeletal_Arsonist), [Skeletal Reaver](https://poe2db.tw/us/Skeletal_Reaver), [Skeletal Storm Mage](https://poe2db.tw/us/Skeletal_Storm_Mage) (PoE2DB), tier 2, crawl 2026-11-23
- Confidence: single-source
- Notes: see [[gems/minion-skills]].

## Carried over from earlier version (2026-11-17)
- Claim: Shocked Ground shocks anyone standing on it, 6 s default. Shock chance is rolled per hit (no stacking debuff) — [INFERRED] from the absence of a shock-chance debuff keyword. Shock also raises ailment damage taken ([[mechanics/ignite]], [[mechanics/poison]], [[mechanics/bleed]]).
- Version: 0.5.5.9 · Volatility: may-change
- Source: RePoE poe2 keywords.json "Shocked Ground", "Shock", tier 2, retrieved 2026-11-17
- Confidence: single-source (game data)

- Claim: Most monsters' ailment threshold ≈ their max life; Unique bosses and some Rares have lower relative thresholds. No numeric table published. Poison and bleed chance don't use the threshold (static chance).
- Version: 0.5.x · Volatility: may-change
- Source: [Mobalytics Chill](https://mobalytics.gg/poe-2/guides/chill), [Mobalytics Ailments](https://mobalytics.gg/poe-2/guides/ailments), tier 3; [poe2wiki Contributes](https://poe2wiki.net/wiki/Contributes), tier 2 (snippet); retrieved 2026-11-17
- Confidence: confirmed (2+ sources)
