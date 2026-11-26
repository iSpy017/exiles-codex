# Attack, Cast & Skill Speed

Status: partial — use-time formula and dual-wield rules added 2026-11-25; weapon base rates by class and reload specifics still missing. Re-check at 1.0.

## Attacks use the weapon; spells use the skill
- Claim: An attack's base damage, attack speed and crit come from the equipped weapon unless the skill says otherwise. Spells have their own base damage, cast time and crit, and ignore weapon stats.
- Version: 0.5.x
- Volatility: stable
- Source: [poe2wiki Attack](https://www.poe2wiki.net/wiki/Attack), tier 2; [PoE2DB Keywords](https://poe2db.tw/us/Keywords), tier 2; retrieved 2026-11-17
- Confidence: confirmed

## Skill speed stacks additively with attack/cast speed
- Claim: "Skill Speed" affects every skill and adds together with the narrower variants (attack speed incl. crossbow reload, cast speed, trap throw speed, totem placement, warcry speed, reload speed) into one total. E.g. 6% inc cast + 5% inc skill = 11% for spells.
- Version: 0.5.x
- Volatility: may-change
- Source: [poe2wiki Skill speed](https://www.poe2wiki.net/wiki/Attack_speed), tier 2, rev 130082, read via built-in browser 2026-11-25; [Mobalytics Skill Speed](https://mobalytics.gg/poe-2/guides/skill-speed), tier 3, 2026-11-17
- Confidence: confirmed

## Use-time formula
- Claim: Final use time = base use time ÷ (1 + total skill speed%) + any flat time penalty. E.g. 0.8 s base (1.25/s) with 40% inc → 1.75/s → 0.57 s.
- Version: 0.5.x
- Volatility: stable
- Source: poe2wiki Skill speed, tier 2, 2026-11-25
- Confidence: single-source

## Fixed use-time penalties can't be sped up
- Claim: Some skills carry a flat penalty (e.g. Whirling Assault "+1 second to Total Attack Time"). It's added after speed modifiers, so speed stats don't shrink it.
- Version: 0.5.x
- Volatility: may-change
- Source: poe2wiki Skill speed, tier 2, 2026-11-17 and 2026-11-25
- Confidence: single-source

## Server-frame cap
- Claim: Non-channelled actions happen at most once per 33 ms server frame (~30.3/s). Faster use times lose DPS even though the tooltip still counts them.
- Version: 0.5.x
- Volatility: may-change
- Source: poe2wiki Skill speed, tier 2, 2026-11-25
- Confidence: single-source

## Action speed is different
- Claim: Action speed is a separate multiplier from skill speed and is what slows (e.g. chill) reduce.
- Version: 0.5.x
- Volatility: may-change
- Source: poe2wiki Skill speed, tier 2, 2026-11-25; [Mobalytics Skill Speed explained](https://mobalytics.gg/poe-2/profile/dreamcore/guides/poe-2-skill-speed-explained), tier 3, 2026-11-17
- Confidence: confirmed

## Local weapon attack speed
- Claim: "% increased Attack Speed" on a weapon modifies that weapon's base attack speed and is multiplicative with global attack speed.
- Version: 0.5.x
- Volatility: stable
- Source: [poe2wiki Modifier](https://www.poe2wiki.net/wiki/Modifier), tier 2, rev 135639, 2026-11-25
- Confidence: single-source; see [[mechanics/damage-calculation]] for other local mods.

## Dual wielding
- Claim: Dual wielding = a martial weapon in each hand, both the same item class. Caster weapons, spears and flails can't be dual wielded, which leaves maces, swords, axes and daggers. Two empty hands don't count. No inherent bonus (unlike PoE1's 10% more attack speed). Two one-handed swords grant Parry only if a sword is in the off-hand. Two-handed axes/maces/swords can be dual wielded with Giant's Blood or The Bringer of Rain.
- Version: 0.5.x
- Volatility: may-change (1.0 adds Duelist)
- Source: [poe2wiki Dual wielding](https://www.poe2wiki.net/wiki/Dual_wielding), tier 2, rev 135854, 2026-11-25
- Confidence: single-source
- Notes: an older revision snippet ([poe2wiki Dual wield](https://poe2wiki.net/wiki/Dual_wield)) only says "same item class"; the newer list may exclude claws because no claws are dual-wieldable in 0.5 — [INFERRED], check at 1.0.

## Dual-wield hits: alternate or combined
- Claim: The skill decides: it alternates hands, or uses both for one combined hit. In a combined hit each hand rolls separately and the damage is summed; one hand critting makes the whole hit a crit. If one weapon can't be used by the skill, only the compatible one is used.
- Version: 0.5.x
- Volatility: may-change
- Source: poe2wiki Dual wielding, tier 2, 2026-11-25
- Confidence: single-source; conflicts with a PoB-PoE2 pull request saying "double hits when dual wielding" skills make two separate hits — see [[04-conflicts]].

## Onslaught
- Claim: Onslaught grants 20% increased Skill Speed.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Keywords](https://poe2db.tw/us/Keywords), tier 2, retrieved 2026-11-17
- Confidence: single-source

## Still to source
- Weapon base attack rates by class; dual-wield attack rate when the two weapons differ; reload speed specifics; warcry speed specifics.
