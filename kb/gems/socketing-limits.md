# Socketing & Gem Slot Limits

Version: 0.5.x (researched 2026-11-17). Re-check at 1.0.

## Skill gem slots
- Claim: Characters have 9 skill gem slots by default; some classes/ascendancies (e.g. Gemling Legionnaire) add more.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB early-access notes](https://poe2db.tw/markdown_raw?oldid=556), tier 2; Deltia's Gaming skill gems guide, tier 5; retrieved 2026-11-17
- Confidence: single-source (tier 2) — verify current number in game
- Notes: Unset Ring implicit grants +1 skill slot ([[items/bases-implicits]]).

## Support sockets per skill
- Claim: Each skill gem starts with 2 support sockets and can go up to 5. Lesser Jeweller's Orb sets a skill gem to 3 support sockets, Greater sets it to 4, Perfect sets it to 5 (each sets the count; it doesn't add one).
- Version: 0.5.5.9
- Volatility: may-change
- Source: [RePoE poe2 base_items.json](https://github.com/repoe-fork/poe2) currency descriptions, tier 2 (game data), retrieved 2026-11-17; [Mobalytics Skill Gem System](https://mobalytics.gg/poe-2/guides/skill-gem-system), tier 3 (2 → 5)
- Confidence: confirmed (game text)
- Notes: Drop levels: Lesser 25, Greater 45, Perfect 65. Earlier conflict (Poe-Vault vs old PoE2DB text) resolved by game data — see [[04-conflicts]]. Item-granted skills get sockets by item/character level, not Jeweller's Orbs. Vaal Orb on a gem can also add a socket or remove one ([[items/corruption]]).

## Attribute cost of supports
- Claim: Each support socketed raises one attribute requirement of the skill by +5 (the support's colour).
- Version: 0.5.x
- Volatility: may-change
- Source: [Mobalytics Skill Gem System](https://mobalytics.gg/poe-2/guides/skill-gem-system), tier 3; support entries show "Support Requirements: +5 Str/Dex/Int" on [poe2wiki Lineage Supports](https://www.poe2wiki.net/wiki/Lineage_Supports), tier 2; game keyword "Support Gem Requirements" (cumulative, generally +5 per support); retrieved 2026-11-17
- Confidence: confirmed

## Duplicate rules
- Skills: since 0.3.0 you can't socket two copies of the same skill gem in your main skill slots (skills not from gems, and skills inside persistent/meta gems, don't count; spectres/beasts: one of each monster).
- Supports — category: you can't socket two supports of the same category in one skill.
- Supports — across skills: CONFLICT. Some poe2wiki pages say one copy of each support per character; poe2wiki's Spirit Gem version history says that restriction was removed ("use as many copies as you like"). → kb/04-conflicts.md.
- Lineage supports: one copy each per character (Solus Ipse bypasses). Gemling's Gem Studded passive also bypasses support-copy limits per poe2wiki.
- Source: [poe2wiki Spirit Gem](https://www.poe2wiki.net/wiki/Spirit_Gem), [poe2wiki Skill gem](https://poe2wiki.net/wiki/Skill_gem), [poe2wiki Gem](https://poe2wiki.net/wiki/Gem), [poe2wiki Abyss lineage support](https://www.poe2wiki.net/wiki/Abyss_lineage_support), tier 2; retrieved 2026-11-17
- Version: 0.5.x, volatility may-change
