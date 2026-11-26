# Spirit & Reservation

Version: game data 0.5.5.9 + 0.5.x sources (researched 2026-11-17). Re-check at 1.0 (campaign changes may move the spirit quests).

## What spirit is
- Claim: Spirit is a pool used to switch on and keep up persistent effects (persistent buffs/auras, heralds, permanent minions, meta gems). Persistent skills are toggled in the Skills Panel. Reserving doesn't lower your maximum — it locks part of it.
- Version: 0.5.5.9
- Volatility: may-change
- Source: game keywords "Spirit", "Reservation", "Persistent Skills", "Minions", tier 2 ([RePoE](https://github.com/repoe-fork/poe2)); [Mobalytics Spirit](https://mobalytics.gg/poe-2/guides/spirit), tier 3; retrieved 2026-11-17
- Confidence: confirmed

## Spirit can differ per weapon set
- Claim: Each weapon set can have a different spirit total (e.g. a sceptre in one set, set-specific passives, set-specific persistent skills). If a swap drops your spirit, some reservations may not fit.
- Version: 0.5.5.9
- Volatility: may-change
- Source: game keywords "Spirit", "Weapon Sets", tier 2; [Maxroll Spirit guide](https://maxroll.gg/poe2/guides/spirit-guide), tier 3; retrieved 2026-11-17
- Confidence: confirmed
- Notes: Maxroll advises testing swaps somewhere safe before bosses.

## Campaign spirit: 100 total
- Claim: The campaign gives 100 max spirit in total from three boss/quest rewards (skull items you consume). Still 100 after Cruel difficulty was removed (0.3).
- Version: 0.5.x
- Volatility: may-change — needs-1.0-check (new acts, Interludes removed)
- Source: [Mobalytics Spirit](https://mobalytics.gg/poe-2/guides/spirit), tier 3; Poe-Vault "Does the campaign still grant 100 spirit" (2025-09-10), tier 3; [poe2wiki Spirit](https://poe2wiki.net/wiki/Spirit) (quest items grant spirit), tier 2; retrieved 2026-11-17
- Confidence: confirmed (100 total)
- Notes: exact bosses/amounts per boss → [[campaign/permanent-rewards]]. A source names Act 1's King in the Mists → +30 (tier 5, verify).

## Gear spirit
- Claim: Sceptres have a 100-spirit implicit, and explicit mods can push a sceptre past 200. Amulets and body armours can roll spirit as explicits; the Solar Amulet base has a 10–15 spirit implicit. Some uniques give spirit (e.g. Enfolding Dawn +100).
- Version: 0.5.x
- Volatility: may-change
- Source: [Mobalytics Spirit](https://mobalytics.gg/poe-2/guides/spirit), tier 3; [poe2wiki Spirit](https://poe2wiki.net/wiki/Spirit), tier 2; [PoE2DB Spirit](https://poe2db.tw/Spirit) (unique examples), tier 2; retrieved 2026-11-17
- Confidence: confirmed (sceptre 100, amulet/body explicits); single-source (Solar Amulet range, roll ranges)
- Notes: exact roll tiers → mods.json in the items batch.

## Free (non-reserving) persistents
- Claim: Persistent buffs and permanent minions granted by item implicits (e.g. sceptres) or by ascendancy passives don't reserve spirit.
- Version: 0.5.x
- Volatility: may-change
- Source: [poe2wiki Spirit](https://poe2wiki.net/wiki/Spirit), tier 2, retrieved 2026-11-17
- Confidence: single-source

## Reservation efficiency
- Claim: "Spirit Reservation Efficiency" mods reduce what skills reserve; some are conditional (e.g. per 100 max life for buff skills).
- Version: 0.5.x
- Source: [PoE2DB Spirit](https://poe2db.tw/Spirit), tier 2, retrieved 2026-11-17
- Confidence: single-source
- Notes: link to the user's spirit-gem price lesson in [[strategy/league-lifecycle-pricing]].
