# Uncut Skill, Spirit & Support Gems

Version: game data 0.5.5.9 (base_items.json + skill_gems.json, RePoE) + 0.5.x sources (researched 2026-11-17). Re-check at 1.0.

## Three kinds
- Uncut Skill Gem — engraves an active skill gem, or levels one up.
- Uncut Spirit Gem — engraves a persistent skill gem (buff/aura/herald/permanent minion/meta), or levels one up.
- Uncut Support Gem — engraves a support gem.
- Version: 0.5.5.9
- Source: [RePoE poe2 base_items.json](https://github.com/repoe-fork/poe2) item descriptions, tier 2; [poe2wiki Uncut gem](https://www.poe2wiki.net/wiki/Uncut_gem), tier 2; [Mobalytics Skill Gem System](https://mobalytics.gg/poe-2/guides/skill-gem-system), tier 3; retrieved 2026-11-17
- Confidence: confirmed

## Levels and drop levels (game data)
- Uncut Skill Gem: levels 1–20. Item drop level: L1 1 · L2 4 · L3 7 · L4 11 · L5 15 · L6 19 · L7 23 · L8 27 · L9 32 · L10 37 · L11 42 · L12 47 · L13 53 · L14 59 · L15–20 62.
- Uncut Spirit Gem: levels 4–20 only (lowest is 4). Same drop levels as skill gems from L4 up (L4 11 … L14 59, L15–20 62).
- Uncut Support Gem: levels 1–5. Drop level: L1 1 · L2 16 · L3 33 · L4 45 · L5 55.
- Version: 0.5.5.9
- Volatility: may-change
- Source: [RePoE poe2 base_items.json](https://github.com/repoe-fork/poe2), tier 2; [poe2wiki Uncut gem](https://www.poe2wiki.net/wiki/Uncut_gem) (spirit lowest 4, drop level breakpoints exist, area level 40 normal monster → L10), tier 2; retrieved 2026-11-17
- Confidence: confirmed (spirit min L4); single-source (full drop table)
- Notes: wiki says from drop level 62+ several uncut tiers can drop — so L15–20 all share drop level 62. Earlier patches used fewer fixed levels (poedb old text: skill 1/3/5/7/9/11/13, support 1/2/3, buff 4/8/12) — superseded.

## Gem tiers gate what you can engrave
- Claim: Every cuttable gem has a tier; you need an uncut gem of at least that level to engrave it (e.g. a tier-7 skill needs a L7+ uncut). Same rule for upgrading.
- Version: 0.5.x
- Volatility: may-change
- Source: [Poe-Vault Gems Guide](https://www.poe-vault.com/poe2/guides/gems-guide), tier 3; game data skill_gems.json `crafting_level` matches wiki tiers (Sniper's Mark 7, Fork 3, Pierce III 5), tier 2; retrieved 2026-11-17
- Confidence: confirmed

## Active-skill tiers (game data counts, cuttable gems only)
- Tier 1: 33 · 3: 30 · 4: 24 · 5: 31 · 7: 29 · 8: 15 · 9: 24 · 11: 22 · 13: 24 · 14: 13. (Tiers 2/6/10/12 unused.)
- Spirit/persistent gems sit at tiers 4, 8 and 14 (plus a few minion/meta exceptions), e.g. heralds and Arctic Armour 4; Blink, Defiance Banner 8; Archmage, Berserk, Trinity, Cast on Critical 14.
- Version: 0.5.5.9
- Source: RePoE skill_gems.json, tier 2; [poe2wiki Engraving](https://poe2wiki.net/wiki/Engraving) (persistent tiers IV/VIII/XIV), tier 2; retrieved 2026-11-17
- Confidence: confirmed (persistent tiers 4/8/14)
- Notes: means L4 spirit uncut = first heralds; L8 = second tier; L14 = top persistents. Data includes some "Coming Soon"/[DNT] placeholders — ignored.

## Where gems come from
- Uncut gems drop from monsters (level set by area) and quest rewards. Lineage supports can't be engraved — see [[gems/lineage-supports]].
- Source: [Poe-Vault Gems Guide](https://www.poe-vault.com/poe2/guides/gems-guide), tier 3; [poe2wiki Lineage](https://www.poe2wiki.net/wiki/Lineage), tier 2.

## Price lesson
- See [[strategy/league-lifecycle-pricing]]: low-level uncut spirit gems spike late-league.
