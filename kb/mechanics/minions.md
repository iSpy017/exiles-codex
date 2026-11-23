# Minions

Status: partial — scaling/skill list/spirit table still open.
Version: game data 0.5.5.9 + 0.5.x (researched 2026-11-17; scaling added batch 17). Re-check at 1.0.
"Game keywords" = [RePoE poe2 keywords.json](https://github.com/repoe-fork/poe2), tier 2.

## Types
- Claim: Minions are summoned allies. Persistent minions reserve spirit while active. Reviving minions heal after avoiding damage for a while and revive after a short delay when killed; the delay resets whenever another reviving minion dies. Temporary minions never revive.
- Version: 0.5.5.9
- Volatility: may-change
- Source: game keywords "Minions", "Reviving Minions", "Temporary Minion", tier 2; [poe2wiki Reviving Minions](https://www.poe2wiki.net/wiki/Reviving_Minions), tier 2; retrieved 2026-11-17
- Confidence: confirmed
- Notes: [poe2wiki Minion](https://poe2wiki.net/wiki/Minion) gives the number: revive if no allied minion died in the past 7 s by default.

## Companions
- Claim: Companions are stronger reviving minions; by default only one companion of any type at a time (e.g. a Druid wolf pack counts as one).
- Version: 0.5.5.9
- Source: game keywords "Companions", tier 2; [poe2wiki Reviving Minions](https://www.poe2wiki.net/wiki/Reviving_Minions), tier 2; retrieved 2026-11-17
- Confidence: confirmed

## Reforming / died vs killed / commands / offerings
- Claim: Dead persistent minions get a "Minion Reforming" timer and return when it ends. Minions that expire or are despawned "died" but weren't "killed" — kill-triggers only fire at 0 life. Command skills order one minion; Offering skills target a Skeleton to make a damageable Offering Spike with buffs.
- Version: 0.5.5.9
- Source: game keywords "Minion Reforming", "Minion Death and Killing Minions", "Minion Commands", "Offering Skills", tier 2, retrieved 2026-11-17
- Confidence: single-source (game data)

## Minion level vs gem level
- Claim: Minion level = 2 × gem level (gem L1 → minion L2 … gem L40 → minion L80). Minion Mastery support gives +1 level to supported minion skills.
- Version: 0.5.x
- Volatility: may-change
- Source: [PoE2DB Minions](https://poe2db.tw/us/Minions), tier 2, retrieved 2026-11-17
- Confidence: single-source
- Notes: "very underleveled" minions get an energy-generation penalty with Cast on Minion Death (same page).

## Which player modifiers reach minions
- Claim: There is no general inheritance rule. Minions use their own modifiers; effects pass through only where an item/passive/gem says so. Examples (PoE2DB): Carrion Call — minion res = yours, more minion max life; Loyalty / Romira's Requital — minions take part of your hit damage, lower max life; Tangmazu's Thurible — companion evasion/deflection based on yours; Chober Chaber / Trenchtimbre — minion damage / attack-speed mods also affect you; Umbilicus Immortalis — your life flask also applies to minions.
- Version: 0.5.x
- Source: [PoE2DB Minions](https://poe2db.tw/us/Minions), tier 2, retrieved 2026-11-17 (page truncated at 100k of 387k chars)
- Confidence: single-source; "no general rule" is the page's own lack of an inheritance section — [INFERRED] absence, verify with a build

## Spirit
- Claim: Only Skeletal Warrior has a stated reservation on the page: 20 spirit at gem level 20, first 2 minions free of base reservation. Enormity (Hulking Minions) support raises spirit cost, no number. Reservation-efficiency mods exist on items (e.g. The Raven's Flock 30–50% increased).
- Version: 0.5.x
- Source: [PoE2DB Minions](https://poe2db.tw/us/Minions), tier 2, retrieved 2026-11-17
- Confidence: single-source; full per-skill table not captured → [[mechanics/spirit-reservation]]

## Not yet sourced
- Minion skill list and per-skill spirit costs (skill_gems.json); minion base life/damage per level; remainder of PoE2DB Minions page (offset 100000+).
