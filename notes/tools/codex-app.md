# Exile's Codex — KB search app

- Live site: https://ispy017.github.io/exiles-codex/ (installable PWA, works offline after first visit). Repo: https://github.com/iSpy017/exiles-codex (public — everything in it is public).
- Old claude.ai artifact (https://claude.ai/artifact/SZQKiCSqH4ycn3Px1FQDLb) is frozen at the 2026-11-23 afternoon snapshot; the GitHub site replaces it.
- Repo layout: `kb/` (markdown copies of the project docs), `data/mods/` (parsed poe2db mod data), `app/` (index.html, db.js, sw.js, manifest, icons), `tools/build_index.py` (kb/ → kb.json), `tools/build_data.py` (crawl zips → data/mods). Every push to `main` runs the GitHub Action that builds and deploys to Pages (~25 s).
- Contents as of 2026-11-23: 99 KB docs (02-sources and tools/ excluded from search), 692 entries, 567 named items; mod database = 87 item-class pages, 26,374 mods from the PoE2DB crawl of 2026-11-23 ([[tools/poe2db-corpus]]), incl. pages that already look like 1.0 content (Daggers, Flails, Swords, Traps, Trarthan Cannon, Temple Tablet).
- Mod tiers in the app are ranked by mod level within each stat line (higher = better); weight = PoE2DB spawn weight. Each class links back to its PoE2DB page (CC BY-NC-SA 3.0 credit in footer and README; non-commercial, no ads).
- Refresh KB (when David says "rebuild the app"): read the changed project docs, write them into the repo's `kb/`, commit, push. Refresh mods: David runs the crawler + `--pack-only`; Claude stages the zips, runs `python tools/build_data.py <zips> --out data/mods`, commits, pushes.
- Stale rule: volatile entries whose newest date is more than 7 days old are flagged in the browser on the day the page is opened.
