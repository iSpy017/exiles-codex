---
title: Caster & ES mod tiers by item level
status: done
tracker_topic: "Caster & ES mod tiers by item level"
tracker_note: "done (0.5.x RePoE; base ES / weapon base damage not captured)"
---

Version: game data from the RePoE poe2 export (mods.json), pulled 2026-11-23 — 0.5.x. Re-check at 1.0 (200+ new bases, crafting changes).
Source: RePoE poe2 mods.json [S002], tier 2, retrieved 2026-11-23 (`required_level` = item level needed; values = min–max roll). Single-source (game data). Usage notes → [[sources]].
Companion: +spell-level ladders and boots movement speed → [[builds/levelling-gear]]; how item level is set → [[items/item-level]].

## % increased Spell Damage (prefix)
| ilvl | Wand / Focus | Staff | Amulet |
|---|---|---|---|
| 1 | 25–34 | 50–68 | 3–7 |
| 8 | 35–44 | 69–88 | — |
| 16 | 45–54 | 89–108 | 8–12 |
| 33 | 55–64 | 109–128 | 13–17 |
| 46 | 65–74 | 129–148 | 18–22 |
| 60 | 75–89 | 149–188 | 23–26 |
| 70 | 90–104 (wand only) | 189–208 | — |
| 75 | — | — | 27–30 |
| 80 | 105–119 (wand only) | 209–238 | — |

## % increased Cold Damage (prefix)
| ilvl | Wand / Focus | Staff | Ring |
|---|---|---|---|
| 2 | 25–34 | 50–68 | — |
| 8 | 35–44 | 69–88 | 3–7 |
| 16 | 45–54 | 89–108 | 8–12 |
| 33 | 55–64 | 109–128 | 13–17 |
| 46 | 65–74 | 129–148 | 18–22 |
| 60 | 75–89 | 149–188 | — |
| 65 | — | — | 23–26 |
| 70 | 90–104 (wand) | 189–208 | — |
| 75 | — | — | 27–30 |
| 81 | 105–119 (wand) | 209–238 | — |
- Notes: [INFERRED] spell damage and cold damage are separate mod groups, so a staff can roll both (two prefixes). Staffs and wands also carry the +spell-level prefixes ([[builds/levelling-gear]]) — prefixes are limited to 3 on a rare ([[items/rarity]]), so +levels compete with % damage.

## % increased Cast Speed (suffix)
| ilvl | Wand / Focus | Staff | Ring / Amulet |
|---|---|---|---|
| 1 | 9–12 | 14–19 | 9–12 |
| 15 | 13–16 | 20–25 | — |
| 18 | — | — | 13–15 |
| 30 | 17–20 | 26–31 | — |
| 35 | — | — | 16–18 |
| 45 | 21–24 | 32–37 | — |
| 51 | — | — | 19–21 |
| 60 | 25–28 | 38–43 | 22–24 |
| 70 | 29–32 (focus/wand) | 44–49 | — |
| 80 | 33–35 (wand) | 50–52 | — |
- Amulet top tier 25–28 at ilvl 66.

## % increased Critical Hit Chance for Spells (suffix)
| ilvl | Wand / Focus | Staff |
|---|---|---|
| 11 | 27–33 | 40–49 |
| 21 | 34–39 | 50–59 |
| 28 | 40–46 | 60–69 |
| 41 | 47–53 | 70–79 |
| 59 | 54–59 | 80–89 |
| 76 | 60–73 (wand) | 90–109 |

## Energy shield
@ v=0.5.x vol=may-change conf=single-source date=2026-11-23 fill=src
- Flat local ES on Int armour pieces: 10–17 (ilvl 1) · 25–30 (16) · 31–35 (25) · 36–41 (33) · 42–47 (46) · 48–60 (54) · 61–73 (60) · 74–80 (65) · 81–90 (70) · 91–96 (79).
- % increased local ES on Int armour: 15–26 (2) · 27–42 (16) · 43–55 (33) · 56–67 (46) · 68–79 (54) · 80–91 (60) · 92–100 (65); body armour only 101–110 (75).
- Flat max ES on amulets: 8–14 (1) · 15–20 (11) · 21–24 (16) · 25–33 (25) · 34–41 (33) · 42–51 (46) · 52–61 (54) · 62–70 (65) · 71–79 (70) · 80–89 (80).
- conf: single-source (game data)
- notes: item base ES (before mods) is not in this doc → gap (PoE2DB base pages / base_items.json).
