# Gem Level vs Character Level

Version: 0.5.x / game data 0.5.5.9 (researched 2026-11-17). Re-check at 1.0.

## Required character level per gem level
- Claim: Gem level → required character level (persistent/skill gem example, Herald of Ice):

| Gem lvl | Char lvl | Gem lvl | Char lvl |
|---|---|---|---|
| 1 | — (0) | 11 | 41 |
| 2 | 3 | 12 | 46 |
| 3 | 6 | 13 | 52 |
| 4 | 10 | 14 | 58 |
| 5 | 14 | 15 | 64 |
| 6 | 18 | 16 | 66 |
| 7 | 22 | 17 | 72 |
| 8 | 26 | 18 | 78 |
| 9 | 31 | 19 | 84 |
| 10 | 36 | 20 | 90 |

- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Herald of Ice](https://poe2db.tw/us/Herald_of_Ice) level table, tier 2, retrieved 2026-11-17; endpoints cross-checked: [Mobalytics High Level Gems](https://mobalytics.gg/poe-2/guides/high-level-gems) (L20 needs char 90), [Mobalytics spell gem database](https://mobalytics.gg/poe-2/database/spell-skill-gems) (persistent gem levels 4–20 require char 10–90), tier 3
- Confidence: confirmed (L4 = 10, L20 = 90); single-source for the middle rows
- Notes: [INFERRED] the same schedule applies to all skill/spirit gems (the Mobalytics ranges match for every gem listed) — spot-check another gem when convenient. Attribute requirements also rise with level and +5 per socketed support ([[gems/socketing-limits]]).

## Answers the spirit-gem seed question
- L8 spirit gem → char level 26 · L9 → 31 · L10 → 36 · L12 → 46.
- So the [[strategy/league-lifecycle-pricing]] play (sell campaign L8, buy L10/L12) needs char 36 for L10 and 46 for L12.

## Uncut gems make gems at their own level
- Claim: An uncut gem engraves a gem at the uncut gem's level; the same uncut gems also level up existing gems. Higher uncut gems drop in higher-level areas.
- Version: 0.5.x
- Source: [poe2wiki Skill gem](https://poe2wiki.net/wiki/Skill_gem), [poe2wiki Uncut gem](https://www.poe2wiki.net/wiki/Uncut_gem), tier 2; [Poe-Vault Gems Guide](https://www.poe-vault.com/poe2/guides/gems-guide), tier 3; retrieved 2026-11-17
- Confidence: confirmed
- Details in [[gems/uncut-gems]].

## Gem levels above 20
- Claim: Level 20 is the normal cap. Corrupting (Vaal Orb) can add +1 level, and the +1 stays as you level it — so corrupt a low gem, then raise it with a L20 uncut gem to reach L21. Item/support bonuses ("+X to level") stack on top.
- Version: 0.5.x
- Volatility: may-change
- Source: [Maxroll Corruption outcomes](https://maxroll.gg/poe2/resources/corruption-outcomes), tier 3; [Mobalytics Level 21 gems guide](https://mobalytics.gg/poe-2/guides/level-21-skill-gems-guide-by-ignatius), tier 3; [poe2wiki Corrupted](https://poe2wiki.net/wiki/Corrupted) (corrupted gems can still be levelled with uncut gems), tier 2; retrieved 2026-11-17
- Confidence: confirmed
- Notes: Mobalytics' method uses an Omen of Corruption with the Vaal Orb → [[crafting/omens]], [[items/corruption]].
