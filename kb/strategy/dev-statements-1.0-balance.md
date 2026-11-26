---
title: 1.0 Dev Statements — balance, classes, crafting, new-player changes (pre-patch-notes)
status: done
tracker_topic: "1.0 dev statements — balance/classes/crafting"
tracker_note: "done (tier-1 interviews + tier-5 rumours; volatile)"
defaults: v=1.0 vol=volatile
---

Sources (YouTube transcripts supplied by David, TranscriptX.ai, ingested 2026-11-17; ASR errors possible):
- [A] "Behind the Scenes Interview with Jonathan & Mark … ExileCon 2026 | FULL INTERVIEW" — GGG's Jonathan and Mark. Tier 1 (staff), via transcript.
- [B] "Path of Exile 2 Thailand Interview Reaction" — Jonathan answers; creator commentary excluded. Tier 1 for Jonathan's lines.
- [C] "ExileCon Highlights and Path of Exile 2 Impressions" — a creator's recollections of demos and dev chats. Tier 5: leads only.
Version: 1.0 pre-release. Volatility: volatile — all subject to the 1.0 patch notes. Re-check each line then.

## Crit chance leaves the passive tree
@ v=1.0 vol=may-change conf=confirmed date=2026-11-17
Crit chance is no longer on the passive tree in 1.0; gear gives crit chance and the tree amplifies crit damage. Daggers and traps are the highest-crit weapon types (Shadow daggers ~25% base crit; ~60% overall crit is still reachable). GGG wants to end "reach 100% and stay there". Crit on jewels is also being cut back (five-mod jewel bug fixed, see below). [C] adds that plus-levels on a 2H trap looked nerfed (trap showed +1 vs a 2H mace minimum of +2) — [INFERRED], one demo observation.
- src: [A] Jonathan/Mark, tier 1 via transcript; [C] tier 5; retrieved 2026-11-17
- conf: confirmed that crit is off the tree ([A] and [C] agree); numbers single-source
- notes: Existing docs written for 0.5.5.9 → [[mechanics/crit]], [[classes/passive-tree]], [[builds/starter-archetypes]]; all need the 1.0 check. Jonathan: crit-heavy "spiky" builds are intended for Shadow.


## Nerfs and balance stance
@ v=1.0 vol=volatile conf=single-source date=2026-11-17
Many 1.0 nerfs coming; top comes down, bottom up. Jonathan confirmed Gemling Legionnaire skill-quality nerfs were finished before 0.5.5 and not yet shown. Crit changes reduce Cast on Critical consistency; [C] heard (unconfirmed) that one skill/spirit gem is being removed, guessed to be Cast on Crit. Balance effort is aimed at the new-player experience (fewer "noob trap" supports, better recommended supports).
- src: [B] and [A] Jonathan, tier 1 via transcript; [C] rumour, tier 5; retrieved 2026-11-17
- conf: single-source; rumour unverified
- notes: David's 0.5.5 practice build (Ice Shot Deadeye) is crit-based → see [[strategy/practice-build-0.5.5]] for a re-judge.


## Poison and bleed
@ v=1.0 vol=may-change conf=single-source date=2026-11-17
1.0 adds necrotic poison (regular poison converted by skills; stacks without limit) so poison gets combo gameplay like bleed's "blood loss" consumers. Poison support gems will be added for Ranger. [C] adds a third kind, gaseous poison (one stack) and says Chayula's Unraveling becomes Threads of Chaos, letting chaos damage contribute to ignite/shock/freeze by choice; these two details are tier 5.
- src: [A] Jonathan (necrotic poison, blood loss), tier 1 via transcript; [C], tier 5; retrieved 2026-11-17
- conf: single-source (A); [C] unverified
- notes: Current rule: poison stack limit 1 → [[mechanics/poison]], [[mechanics/bleed]].


## Classes and ascendancies
@ v=1.0 vol=volatile conf=confirmed date=2026-11-17
1.0 adds Shadow (stealth, daggers, traps) and Duelist (stances, combos, swords). Not every remaining ascendancy for the older classes will make 1.0 (Ranger most likely next). Warrior is being improved with new VFX/animations and mechanics (e.g. slam rocks as a resource). Sorceress core gameplay is the class Jonathan is least happy with (Fusions/infusion). No Energy Blade/Spell Blade in this patch; trap will not be a meta skill in 1.0. Third trial planned for Act 4 was cut for time.
- src: [A] and [B] Jonathan, tier 1 via transcript; retrieved 2026-11-17
- conf: confirmed where A and B overlap (new classes, warrior); otherwise single-source
- notes: [[classes/index]] lists 10 classes / 26 ascendancies for 1.0 (from GGG press release); the "not all ascendancies" line may lower that — check at 1.0 notes.


## Crafting and currency
@ v=1.0 vol=volatile conf=single-source date=2026-11-17
1.0 adds a fractured-item crafting mechanic and about 15 new currencies. Early currencies are intentionally simple (replace-a-mod style) and have level ranges so they're not hoarded to endgame. Jonathan wants crafting where doing "what it says on the tin" is simple but endgame implications are deep, and wants limited determinism so the best items stay a chase. The five-mod jewel exploit (via a chaos-orb trick) was a bug, not intended; not in the eternal/1.0 build.
- src: [A] Jonathan, tier 1 via transcript; retrieved 2026-11-17
- notes: [[crafting/league-crafting]] and [[crafting/currency-index]] are 0.5.5.9; refresh at 1.0. Jonathan in [B]: uniques are a big 1.0 focus, with wide roll ranges so Divines get sunk into them.


## Item rarity (magic find)
@ v=1.0 vol=may-change conf=single-source date=2026-11-17
GGG would remove increased item rarity if they had a replacement stat, but see it as a third scaling axis. Players dislike that rarity raises currency drops; GGG may fix it, but doing so exactly is tricky with the item-drop model. Rarity was nerfed earlier, not changed in 1.0 so far.
- src: [B] Jonathan, tier 1 via transcript, 2026-11-17
- v: 1.0 (unchanged so far)
- notes: Community view that rarity is optional → [[strategy/rarity-value]]. Mechanics → [[items/rarity]].


## Campaign and new-player changes
@ v=1.0 vol=volatile conf=single-source date=2026-11-17
Permanent campaign rewards are not changeable yet (e.g. Shark Fin, toxins, tattoo); Jonathan said he'd ask Mark to fix it. Interludes are going away (talk in [B] assumes it). Controller UI and mouse can be mixed; GPU optimisation is next focus; the 1.0 client download is large. Servers will be provisioned for launch; DoS protection said to be in place. Champion rares added to the campaign may appear in endgame (Jonathan: "probably should").
- src: [B] and [A] Jonathan, tier 1 via transcript; creator's statement of which rewards are fixed is tier 5; retrieved 2026-11-17
- notes: → [[campaign/permanent-rewards]], [[campaign/interludes]].
