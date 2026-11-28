/* Mod database view: lazy-loads data/mods/<class>.json from the parsed poe2db crawl. */
window.DB = (() => {
  const E = s => String(s ?? '').replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  const N = s => String(s).toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '');
  const KIND = { prefix: 'pre', suffix: 'suf', implicit: 'imp', corrupted: 'cor' };
  let idx = null, cache = {}, f = { cls: '', q: '', kind: '', group: 'normal', ilvl: '', tag: '', top: false };
  try { Object.assign(f, JSON.parse(localStorage.getItem('codex-db') || '{}')); } catch (e) {}
  const save = () => { try { localStorage.setItem('codex-db', JSON.stringify(f)); } catch (e) {} };
  const R = () => document.getElementById('reader');

  async function loadIndex() {
    if (idx) return idx;
    try { const r = await fetch('data/mods/index.json'); idx = r.ok ? await r.json() : { classes: [] }; }
    catch (e) { idx = { classes: [] }; }
    return idx;
  }
  async function loadClass(key) {
    if (!cache[key]) { const r = await fetch(`data/mods/${encodeURIComponent(key)}.json`); cache[key] = await r.json(); }
    return cache[key];
  }
  function rows(page) {
    const toks = N(f.q).split(/\s+/).filter(Boolean), il = parseInt(f.ilvl, 10);
    let ms = page.mods.filter(m =>
      (!f.group || m.g === f.group) && (!f.kind || m.k === f.kind) && (!f.tag || m.tags.includes(f.tag)) &&
      (!il || (m.lvl ?? 0) <= il) && toks.every(t => N(m.t + ' ' + m.n + ' ' + m.fam).includes(t)));
    if (il || f.top) { // best tier still rollable per family
      const best = {};
      ms.forEach(m => { const k = m.s; if (!best[k] || (m.lvl ?? 0) > (best[k].lvl ?? 0)) best[k] = m; });
      if (f.top) ms = Object.values(best);
      else ms.forEach(m => { m._best = best[m.s] === m; });
    }
    return ms.sort((a, b) => a.k.localeCompare(b.k) || a.fam.localeCompare(b.fam) || (b.lvl ?? 0) - (a.lvl ?? 0));
  }
  async function show(q) {
    if (q != null) f.q = q;
    const ix = await loadIndex();
    if (!ix.classes.length) {
      R().innerHTML = `<h1>Mod database</h1><p class="empty">The mod data isn't in this build yet. It appears once the poe2db crawl has been parsed and pushed.</p>`;
      return;
    }
    if (!f.cls || !ix.classes.find(c => c.key === f.cls)) f.cls = ix.classes[0].key;
    const meta = ix.classes.find(c => c.key === f.cls), page = await loadClass(f.cls);
    const groups = meta.groups, tags = [...new Set(page.mods.flatMap(m => m.tags))].sort();
    if (!groups.includes(f.group)) f.group = groups.includes('normal') ? 'normal' : '';
    const lab = g => (ix.groupLabels || {})[g] || g;
    R().innerHTML = `<h1>Mod database</h1><div class="path">${ix.classes.length} item classes from poe2db · this class fetched ${E((meta.fetched || '').slice(0, 10))}</div>
    <div class="dbf">
      <label>Item class<select id="dbcls">${ix.classes.map(c => `<option value="${E(c.key)}"${c.key === f.cls ? ' selected' : ''}>${E(c.title)} (${c.count})</option>`).join('')}</select></label>
      <label class="grow">Mod text<input id="dbq" type="search" value="${E(f.q)}" placeholder="e.g. life, cold res, movement"></label>
      <label>Affix<select id="dbk"><option value="">Any</option>${['prefix', 'suffix', 'implicit', 'corrupted'].map(k => `<option${k === f.kind ? ' selected' : ''}>${k}</option>`).join('')}</select></label>
      <label>Source<select id="dbg"><option value="">All sources</option>${groups.map(g => `<option value="${g}"${g === f.group ? ' selected' : ''}>${E(lab(g))}</option>`).join('')}</select></label>
      <label>Tag<select id="dbt"><option value="">Any tag</option>${tags.map(t => `<option${t === f.tag ? ' selected' : ''}>${E(t)}</option>`).join('')}</select></label>
      <label>Item level<input id="dbil" type="number" min="1" max="100" value="${E(f.ilvl)}" placeholder="any"></label>
      <label>&nbsp;<button class="tbtn" id="dbtop" aria-pressed="${f.top}">${f.top ? '✓ ' : ''}Top tier only</button></label>
    </div><div id="dbout"></div>`;
    draw(page);
    const on = (id, ev, fn) => document.getElementById(id).addEventListener(ev, fn);
    on('dbcls', 'change', e => { f.cls = e.target.value; f.tag = ''; save(); show(); });
    on('dbq', 'input', e => { f.q = e.target.value; save(); draw(page); });
    on('dbk', 'change', e => { f.kind = e.target.value; save(); draw(page); });
    on('dbg', 'change', e => { f.group = e.target.value; save(); draw(page); });
    on('dbt', 'change', e => { f.tag = e.target.value; save(); draw(page); });
    on('dbil', 'input', e => { f.ilvl = e.target.value; save(); draw(page); });
    on('dbtop', 'click', e => { f.top = !f.top; save(); show(); });
  }
  function draw(page) {
    const ms = rows(page), il = parseInt(f.ilvl, 10);
    document.getElementById('dbout').innerHTML = `<p class="rcount">${ms.length} mods${il ? ` rollable at item level ${il} (★ = best tier available)` : ''}.
      Higher tier = stronger (PoE2 numbering). Weight = poe2db spawn weight.</p>
      <div class="scroll"><table class="mt"><thead><tr><th>Affix</th><th>Type</th><th>Tier</th><th>Mod lvl</th><th>Effect</th><th>Weight</th></tr></thead><tbody>
      ${ms.slice(0, 600).map(m => `<tr><td class="n">${E(m.n) || '—'}</td><td class="${KIND[m.k] || ''}">${E(m.k)}</td>
        <td class="r">${m._best ? '★ ' : ''}${m.tier}/${m.tiers}</td><td class="r">${m.lvl ?? '—'}</td>
        <td>${E(m.t).replace(/([a-z)%])(?=[A-Z(])|([a-z])(?=%)/g, '$1$2<br>')}<br>${m.tags.map(t => `<span class="tg">${E(t)}</span>`).join('')}</td><td class="r">${m.w ?? '—'}</td></tr>`).join('')}
      </tbody></table></div>${ms.length > 600 ? '<p class="rcount">Showing first 600 — narrow the filters.</p>' : ''}
      <p class="foot">Data: <a href="${E(page.url)}" target="_blank" rel="noopener">poe2db.tw — ${E(page.title)}</a>, fetched ${E((page.fetched || '').slice(0, 10))}, licensed CC BY-NC-SA 3.0. Tier is ranked by mod level within each stat line; check in game before an expensive craft.</p>`;
  }
  return { show };
})();
