/* Exchange margin view (#ce): reads a Currency Exchange order book and works out the first-in-line flip.
   Pure functions are exported for node tests (tools/test_exchange.js); show() renders into #reader.
   Ratio convention: "R : 1" = R units of the wanted item X per 1 unit of the offered item Y. */

// David's provisional thresholds and assumptions — not game facts. All editable on the page.
const CE_TIGHT = 0.05;      // spread below this = tight (flippable)
const CE_THIN = 0.50;       // spread above this = illiquid
const CE_TICK = 0.01;       // smallest ratio step [INFERRED from two-decimal ratios on screen; creator "undercut by .01"]
const CE_STOCK_UNIT = 'X';  // which unit "Stock" counts on the Competing side — unconfirmed

const CE = (() => {
  const E = s => String(s ?? '').replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  const clean = x => Math.round(x * 1e8) / 1e8;  // strip float noise (22.5 - 0.01 = 22.49)

  // ---------- pure logic ----------
  const NUM = '(\\d+(?:\\.\\d+)?|\\.\\d+)';
  const RATIO_RE = new RegExp(`^([<>])?\\s*${NUM}\\s*(?::\\s*${NUM})?$`);
  const ROW_RE = new RegExp(`^([<>])?\\s*${NUM}\\s*(?::\\s*${NUM})?(?:\\s+${NUM})?$`);

  /** "22", "18.50 : 1", "1 : 3", "< 3.05 : 1" → {r, tail, text} or null. */
  function parseRatio(s) {
    const m = String(s ?? '').trim().match(RATIO_RE);
    if (!m) return null;
    const a = parseFloat(m[2]), b = m[3] != null ? parseFloat(m[3]) : 1;
    if (!(a > 0) || !(b > 0)) return null;
    return { r: a / b, tail: m[1] || null, text: ratioText(m[1], m[2], m[3]) };
  }
  const ratioText = (tail, a, b) => (tail || '') + (b != null && parseFloat(b) !== 1 ? `${a}:${b}` : a);

  /** One row per line: ratio then stock. Commas in numbers and either separator style allowed.
      Lines that don't parse are returned in `junk`, never as rows. */
  function parseRows(text) {
    const rows = [], junk = [];
    String(text ?? '').split(/\r?\n/).forEach(line => {
      const raw = line.trim();
      if (!raw) return;
      const t = raw.replace(/(\d),(?=\d{3}(?!\d))/g, '$1').replace(/\s+/g, ' ');
      const m = t.match(ROW_RE);
      if (!m) { junk.push(raw); return; }
      const a = parseFloat(m[2]), b = m[3] != null ? parseFloat(m[3]) : 1, stock = m[4] != null ? parseFloat(m[4]) : null;
      if (!(a > 0) || !(b > 0)) { junk.push(raw); return; }
      rows.push({ r: a / b, tail: m[1] || null, text: ratioText(m[1], m[2], m[3]), stock });
    });
    return { rows, junk };
  }

  const usable = r => r && Number.isFinite(r.r) && r.r > 0 && !r.tail;

  /** Best real (non-tail) row: Available = highest R, Competing = lowest R. */
  function bestOf(rows, side) {
    let best = null;
    for (const r of rows || []) {
      if (!usable(r)) continue;
      if (!best || (side === 'available' ? r.r > best.r : r.r < best.r)) best = r;
    }
    return best;
  }

  const spread = (avail, comp) => comp / avail - 1;
  const midpoint = (avail, comp) => Math.sqrt(avail * comp);

  function label(s, tight = CE_TIGHT, thin = CE_THIN) {
    if (!Number.isFinite(s)) return null;
    if (s < 0) return 'crossed';
    return s < tight ? 'tight' : s <= thin ? 'thin' : 'illiquid';
  }

  /** First-in-line flip, one tick better than the best order on each side. */
  function flipOrders(avail, comp, tick = CE_TICK) {
    if (!(comp - avail > 2 * tick + 1e-9)) return { room: false };
    const buyR = clean(comp - tick), sellR = clean(avail + tick);
    return { room: true, buyR, sellR, margin: buyR / sellR - 1 };
  }

  /** Instant fill of n units of X.
      side 'available': buy n X from sellers (stock counted in X) → cost in Y.
      side 'competing': sell n X to resting buyers (stock in X or Y per stockUnit) → Y received.
      Tail rows count as depth at their bound ratio; `approx` flags when one was used. */
  function depth(rows, n, side, stockUnit = CE_STOCK_UNIT) {
    const live = (rows || []).filter(r => r && r.r > 0 && r.stock > 0);
    const real = live.filter(r => !r.tail).sort((a, b) => side === 'available' ? b.r - a.r : a.r - b.r);
    const tails = live.filter(r => r.tail);
    let left = n, x = 0, y = 0, approx = false;
    for (const r of real.concat(tails)) {
      if (left <= 0) break;
      const capX = side === 'competing' && stockUnit === 'Y' ? r.stock * r.r : r.stock;
      const take = Math.min(left, capX);
      x += take; y += take / r.r; left -= take;
      if (r.tail) approx = true;
    }
    return { filled: clean(x), y: clean(y), avgR: y ? x / y : null, partial: x < n - 1e-9, approx };
  }

  /** Same item priced in currency A (pA) and B (pB); rate = units of A per 1 B.
      aToB = gain from buying in A and selling in B; bToA = the reverse. Before fees. */
  function crossRate(pA, pB, rate) {
    if (!(pA > 0) || !(pB > 0) || !(rate > 0)) return null;
    const g = (pB * rate) / pA;
    return { aToB: g - 1, bToA: 1 / g - 1 };
  }

  /** Full analysis of one book. */
  function analyse(book, opt = {}) {
    const tick = opt.tick ?? CE_TICK, tight = opt.tight ?? CE_TIGHT, thin = opt.thin ?? CE_THIN;
    const a = bestOf(book.avail, 'available'), c = bestOf(book.comp, 'competing');
    if (!a || !c) return { a, c };
    const s = spread(a.r, c.r);
    return { a, c, spread: s, mid: midpoint(a.r, c.r), label: label(s, tight, thin), flip: flipOrders(a.r, c.r, tick) };
  }

  /** Watchlist ranking: margin × fills per hour. Entries without fills/hour or room go last, unranked. */
  function rankWatch(list) {
    return (list || []).map(w => {
      const fph = parseFloat(w.fph), m = w.margin;
      return Object.assign({}, w, { score: fph > 0 && Number.isFinite(m) ? m * fph : null });
    }).sort((p, q) => (q.score ?? -Infinity) - (p.score ?? -Infinity) || String(q.date).localeCompare(String(p.date)));
  }

  const csvCell = v => /[",\n]/.test(String(v)) ? `"${String(v).replace(/"/g, '""')}"` : String(v);
  const CSV_HEAD = 'date,league,want,have,side,ratio_want_per_have,stock';
  /** Rows in the data/prices/*_exchange-books.csv format (no header). */
  function toCSV(book) {
    const out = [];
    for (const [side, rows] of [['available', book.avail], ['competing', book.comp]])
      for (const r of rows || []) if (r && r.r > 0)
        out.push([book.date, book.league, book.want, book.have, side, r.text ?? String(clean(r.r)), r.stock ?? ''].map(csvCell).join(','));
    return out.join('\n');
  }

  // ---------- view ----------
  const KEY = 'codex-ce';
  const today = () => { const d = new Date(); return new Date(d - d.getTimezoneOffset() * 6e4).toISOString().slice(0, 10); };
  const blank = () => ({ want: '', have: '', league: '', avail: [], comp: [] });
  let S = { book: blank(), tick: CE_TICK, unit: CE_STOCK_UNIT, tight: CE_TIGHT * 100, thin: CE_THIN * 100,
            stake: '', n: '', fph: '', cross: { pA: '', a: 'Exalted Orb', pB: '', b: 'Chaos Orb', rate: '' }, watch: [] };
  try { if (typeof localStorage !== 'undefined') S = Object.assign(S, JSON.parse(localStorage.getItem(KEY) || '{}')); } catch (e) {}
  const save = () => { try { localStorage.setItem(KEY, JSON.stringify(S)); } catch (e) {} };
  const $ = id => document.getElementById(id);
  const fR = x => Number.isFinite(x) ? String(clean(Math.round(x * 1e4) / 1e4)) : '—';
  const fP = x => Number.isFinite(x) ? (x * 100).toFixed(2) + '%' : '—';
  const fN = x => Number.isFinite(x) ? (Math.abs(x) >= 100 ? Math.round(x).toLocaleString('en') : String(Math.round(x * 1000) / 1000)) : '—';
  const fPrice = x => Number.isFinite(x) ? String(+x.toPrecision(4)) : '—';
  const opts = () => ({ tick: +S.tick || CE_TICK, tight: (+S.tight || CE_TIGHT * 100) / 100, thin: (+S.thin || CE_THIN * 100) / 100 });
  const X = () => E(S.book.want || 'X'), Y = () => E(S.book.have || 'Y');

  function show() {
    const R = document.getElementById('reader');
    R.innerHTML = `<h1>Exchange margin</h1>
    <div class="path">Currency Exchange order book → first-in-line flip and round-trip margin · saved on this device only</div>
    <p class="cehow">How to read this: paste or type both sides of the pair as shown in game. Ratios are <b>R : 1</b> = R of the item you want per 1 of the item you have.
      Rules: <a href="#strategy-flipping-strats">flipping strategies</a> · mechanics: <a href="#economy-currency-exchange">Currency Exchange</a>.</p>
    <div class="dbf">
      <label class="grow">I want (X)<input id="cewant" value="${E(S.book.want)}" placeholder="e.g. Scroll of Wisdom"></label>
      <label class="grow">I have (Y)<input id="cehave" value="${E(S.book.have)}" placeholder="e.g. Exalted Orb"></label>
      <label class="grow">League<input id="celeague" value="${E(S.book.league)}" placeholder="for the CSV"></label>
    </div>
    <div class="cegrid">${['avail', 'comp'].map(k => `<section class="cebox">
      <h3>${k === 'avail' ? 'Available Trades' : 'Competing Trades'}</h3>
      <p class="rcount">${k === 'avail' ? 'Orders you can fill now. Best = highest R.' : 'Others waiting to buy X with Y. Best = lowest R.'}</p>
      <label class="celbl" for="cepaste-${k}">Paste rows (ratio, stock — one per line)</label>
      <textarea id="cepaste-${k}" rows="4" placeholder="22 : 1   12,187&#10;&lt; 3.05 : 1   139&#10;1 : 3   20"></textarea>
      <div class="cebtns"><button class="tbtn" data-parse="${k}">Replace rows</button><button class="tbtn" data-append="${k}">Add rows</button><button class="tbtn" data-add="${k}">+ empty row</button></div>
      <p class="rcount" id="cejunk-${k}" role="status"></p>
      <div id="cerows-${k}"></div></section>`).join('')}</div>
    <h3>Assumptions</h3>
    <p class="rcount">Not confirmed game facts — change them if you learn better. The gold order fee is left out (gold only costs time).</p>
    <div class="dbf">
      <label>Tick (ratio step)<input id="cetick" type="number" step="0.001" min="0" value="${E(S.tick)}"></label>
      <label>Competing "Stock" counts<select id="ceunit"><option value="X"${S.unit === 'X' ? ' selected' : ''}>X (item wanted)</option><option value="Y"${S.unit === 'Y' ? ' selected' : ''}>Y (item offered)</option></select></label>
      <label>Tight below %<input id="cetight" type="number" step="0.5" min="0" value="${E(S.tight)}"></label>
      <label>Illiquid above %<input id="cethin" type="number" step="1" min="0" value="${E(S.thin)}"></label>
    </div>
    <div class="dbf">
      <label>Stake (Y)<input id="cestake" type="number" min="0" step="any" value="${E(S.stake)}" placeholder="e.g. 100"></label>
      <label>Instant fill N (X)<input id="cen" type="number" min="0" step="any" value="${E(S.n)}" placeholder="e.g. 1000"></label>
      <label>Fills per hour<input id="cefph" type="number" min="0" step="any" value="${E(S.fph)}" placeholder="your estimate"></label>
    </div>
    <div id="ceout" class="cecard" aria-live="polite"></div>
    <h3>Cross-currency check ("trinity trading")</h3>
    <p class="rcount">Same item priced in two currencies, plus the rate between them. Before fees.</p>
    <div class="dbf">
      <label>Price in A<input id="cepa" type="number" min="0" step="any" value="${E(S.cross.pA)}"></label>
      <label class="grow">Currency A<input id="cea" value="${E(S.cross.a)}"></label>
      <label>Price in B<input id="cepb" type="number" min="0" step="any" value="${E(S.cross.pB)}"></label>
      <label class="grow">Currency B<input id="ceb" value="${E(S.cross.b)}"></label>
      <label>A per 1 B<input id="cerate" type="number" min="0" step="any" value="${E(S.cross.rate)}"></label>
    </div>
    <p id="cecross" class="cecard" aria-live="polite"></p>
    <h3>Watchlist</h3>
    <p class="rcount">Saved books, ranked by margin × fills per hour. Stored in this browser only.</p>
    <div class="cebtns"><button class="tbtn" id="cesave">Save current book</button><button class="tbtn" id="cecsv">Copy current as CSV</button><button class="tbtn" id="cecsvall">Copy watchlist as CSV</button></div>
    <p class="rcount" id="cemsg" role="status"></p>
    <div id="cewatch"></div>
    <p class="foot">The tool does the arithmetic only; ratios, stock and fills per hour come from you. Margins on illiquid books assume someone eventually fills both of your orders.</p>`;
    bind();
    ['avail', 'comp'].forEach(drawRows);
    out(); cross(); watch();
  }

  function drawRows(k) {
    const rows = S.book[k];
    $(`cerows-${k}`).innerHTML = rows.length ? `<div class="scroll"><table class="mt cet"><thead><tr><th>Ratio</th><th>Stock</th><th><span class="vh">Remove</span></th></tr></thead><tbody>
      ${rows.map((r, i) => `<tr class="${r.r > 0 ? (r.tail ? 'tail' : '') : 'bad'}"><td><input aria-label="Ratio row ${i + 1}" data-k="${k}" data-i="${i}" data-f="text" value="${E(r.text ?? '')}"></td>
        <td><input aria-label="Stock row ${i + 1}" type="number" min="0" step="any" data-k="${k}" data-i="${i}" data-f="stock" value="${E(r.stock ?? '')}"></td>
        <td><button class="tbtn cex" data-del="${k}" data-i="${i}" aria-label="Remove row ${i + 1}">×</button></td></tr>`).join('')}
      </tbody></table></div><p class="rcount">Rows starting &lt; or &gt; are aggregated tails: counted in depth, never used as best.</p>` : '<p class="empty">No rows yet.</p>';
  }

  function out() {
    const b = S.book, o = opts(), A = analyse(b, o), el = $('ceout');
    if (!A.a || !A.c) { el.innerHTML = `<p class="empty">Needs at least one real (not &lt;/&gt;) row on each side.</p>`; return; }
    const f = A.flip, stake = parseFloat(S.stake), n = parseFloat(S.n), fph = parseFloat(S.fph);
    const tag = { tight: 'tight · flippable', thin: 'thin', illiquid: 'illiquid · post and wait, don’t count on the margin', crossed: 'crossed book · check the rows' }[A.label];
    let h = `<table class="mt"><tbody>
      <tr><th>Best Available</th><td>${fR(A.a.r)} : 1 <span class="st">· 1 ${X()} = ${fPrice(1 / A.a.r)} ${Y()}</span></td></tr>
      <tr><th>Best Competing</th><td>${fR(A.c.r)} : 1 <span class="st">· 1 ${X()} = ${fPrice(1 / A.c.r)} ${Y()}</span></td></tr>
      <tr><th>Spread</th><td><b>${fP(A.spread)}</b> <span class="celab ${A.label}">${tag}</span></td></tr>
      <tr><th>Midpoint</th><td>${fR(A.mid)} : 1 <span class="st">· 1 ${X()} ≈ ${fPrice(1 / A.mid)} ${Y()}</span></td></tr>`;
    if (!f.room) h += `<tr><th>Flip</th><td><b>No room to flip</b> — the two best orders are within two ticks.</td></tr>`;
    else {
      h += `<tr><th>Your buy order</th><td>This pair (want ${X()}, have ${Y()}): <b>${fR(f.buyR)} : 1</b></td></tr>
      <tr><th>Your sell order</th><td>Reverse pair (want ${Y()}, have ${X()}): <b>1 : ${fR(f.sellR)}</b> <span class="st">· ${fR(f.sellR)} ${X()} per ${Y()}</span></td></tr>
      <tr><th>Round-trip margin</th><td><b class="${A.label === 'illiquid' ? 'cewarn' : 'cegood'}">${fP(f.margin)}</b> ${A.label === 'illiquid' ? '<span class="st">illiquid: wide because few trades happen</span>' : ''}</td></tr>`;
      if (stake > 0) h += `<tr><th>Stake ${fN(stake)} ${Y()}</th><td>+${fN(stake * f.margin)} ${Y()} per round trip <span class="st">(or keep ${fN(stake * (f.buyR - f.sellR))} ${X()})</span></td></tr>`;
      if (fph > 0) h += `<tr><th>Score</th><td>${fP(f.margin * fph)} per hour <span class="st">(margin × ${fN(fph)} fills/h)</span></td></tr>`;
    }
    if (n > 0) {
      const d1 = depth(b.avail, n, 'available'), d2 = depth(b.comp, n, 'competing', S.unit);
      const note = d => (d.partial ? ` <span class="cewarn">only ${fN(d.filled)} in the book</span>` : '') + (d.approx ? ' <span class="st">(uses a &lt;/&gt; tail at its bound: approximate)</span>' : '');
      h += `<tr><th>Instant buy ${fN(n)} ${X()}</th><td>${d1.filled ? `avg ${fR(d1.avgR)} : 1 · costs ${fN(d1.y)} ${Y()}` : 'nothing to fill'}${note(d1)}</td></tr>
      <tr><th>Instant sell ${fN(n)} ${X()}</th><td>${d2.filled ? `avg ${fR(d2.avgR)} : 1 · gets ${fN(d2.y)} ${Y()}` : 'nothing to fill'}${note(d2)} <span class="st">(Competing stock read as ${S.unit === 'X' ? X() : Y()})</span></td></tr>`;
    }
    el.innerHTML = h + '</tbody></table>';
  }

  function cross() {
    const c = S.cross, r = crossRate(+c.pA, +c.pB, +c.rate), el = $('cecross');
    if (!r) { el.innerHTML = '<span class="st">Fill in both prices and the rate.</span>'; return; }
    const a = E(c.a || 'A'), b = E(c.b || 'B');
    el.innerHTML = `Buy for ${a}, sell for ${b}: <b class="${r.aToB > 0 ? 'cegood' : 'cewarn'}">${r.aToB >= 0 ? '+' : ''}${fP(r.aToB)}</b> · buy for ${b}, sell for ${a}: <b class="${r.bToA > 0 ? 'cegood' : 'cewarn'}">${r.bToA >= 0 ? '+' : ''}${fP(r.bToA)}</b>
      <span class="st">(${fN(+c.pB)} ${b} = ${fN(c.pB * c.rate)} ${a})</span>`;
  }

  function watch() {
    const L = rankWatch(S.watch.map((w, i) => Object.assign({ i }, w))), el = $('cewatch');
    if (!L.length) { el.innerHTML = '<p class="empty">Nothing saved yet.</p>'; return; }
    el.innerHTML = `<div class="scroll"><table class="mt"><thead><tr><th>Pair</th><th>Saved</th><th>Spread</th><th>Margin</th><th>Fills/h</th><th>Score</th><th><span class="vh">Actions</span></th></tr></thead><tbody>
      ${L.map(w => `<tr><td>${E(w.want)} / ${E(w.have)}</td><td class="r">${E(w.date)}</td><td class="r">${fP(w.spread)} <span class="celab ${E(w.label)}">${E(w.label || '')}</span></td>
        <td class="r">${w.margin == null ? 'no room' : fP(w.margin)}</td><td class="r">${w.fph === '' || w.fph == null ? '—' : E(w.fph)}</td><td class="r">${w.score == null ? 'unranked' : fP(w.score) + '/h'}</td>
        <td class="n"><button class="tbtn" data-load="${w.i}">Load</button> <button class="tbtn" data-wdel="${w.i}" aria-label="Delete ${E(w.want)} / ${E(w.have)}">×</button></td></tr>`).join('')}
      </tbody></table></div>`;
  }

  function msg(t) { $('cemsg').textContent = t; }
  function copy(text, what) {
    if (!text) { msg('Nothing to copy.'); return; }
    const ok = () => msg(`Copied ${what} (${text.split('\n').length - 1} rows + header).`);
    const fallback = () => { const t = document.createElement('textarea'); t.value = text; document.body.appendChild(t); t.select();
      try { document.execCommand('copy'); ok(); } catch (e) { msg('Copy failed — select the text manually.'); } t.remove(); };
    if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(text).then(ok, fallback); else fallback();
  }
  const bookCSV = (bk) => toCSV(Object.assign({}, bk, { date: bk.date || today() }));

  function bind() {
    const R = document.getElementById('reader'), field = { cewant: 'want', cehave: 'have', celeague: 'league' };
    const top = { cetick: 'tick', ceunit: 'unit', cetight: 'tight', cethin: 'thin', cestake: 'stake', cen: 'n', cefph: 'fph' };
    const cx = { cepa: 'pA', cea: 'a', cepb: 'pB', ceb: 'b', cerate: 'rate' };
    R.oninput = R.onchange = e => {
      if (!$('ceout')) return;  // another view owns #reader now
      const t = e.target, id = t.id;
      if (field[id]) { S.book[field[id]] = t.value; out(); }
      else if (top[id]) { S[top[id]] = t.value; out(); }
      else if (cx[id]) { S.cross[cx[id]] = t.value; cross(); }
      else if (t.dataset.k) {
        const row = S.book[t.dataset.k][+t.dataset.i];
        if (t.dataset.f === 'stock') row.stock = t.value === '' ? null : parseFloat(t.value);
        else { const p = parseRatio(t.value); row.text = t.value; row.r = p ? p.r : NaN; row.tail = p ? p.tail : null; if (p) row.text = p.text;
          t.closest('tr').className = p ? (p.tail ? 'tail' : '') : 'bad'; }
        out();
      } else return;
      save();
    };
    R.onclick = e => {
      const t = e.target.closest('button'); if (!t || !$('ceout')) return;
      const d = t.dataset;
      if (d.parse || d.append) {
        const k = d.parse || d.append, ta = $(`cepaste-${k}`), p = parseRows(ta.value);
        S.book[k] = d.parse ? p.rows : S.book[k].concat(p.rows);
        $(`cejunk-${k}`).textContent = `${p.rows.length} rows read${p.junk.length ? ` · ignored ${p.junk.length}: ${p.junk.slice(0, 3).join(' | ')}${p.junk.length > 3 ? ' …' : ''}` : ''}`;
        if (p.rows.length) ta.value = '';
        drawRows(k); out(); save();
      } else if (d.add) { S.book[d.add].push({ r: NaN, tail: null, text: '', stock: null }); drawRows(d.add); save();
        const ins = document.querySelectorAll(`#cerows-${d.add} input[data-f=text]`); ins[ins.length - 1].focus(); }
      else if (d.del) { S.book[d.del].splice(+d.i, 1); drawRows(d.del); out(); save(); }
      else if (t.id === 'cesave') {
        const A = analyse(S.book, opts());
        if (!A.a || !A.c) { msg('Needs a best order on both sides before saving.'); return; }
        const w = { want: S.book.want || 'X', have: S.book.have || 'Y', league: S.book.league, date: today(), fph: S.fph,
          spread: A.spread, label: A.label, margin: A.flip.room ? A.flip.margin : null,
          avail: S.book.avail.filter(r => r.r > 0), comp: S.book.comp.filter(r => r.r > 0) };
        const j = S.watch.findIndex(x => x.want === w.want && x.have === w.have);
        if (j >= 0) S.watch[j] = w; else S.watch.push(w);
        save(); watch(); msg(`Saved ${w.want} / ${w.have} (${w.date}).`);
      } else if (t.id === 'cecsv') copy(CSV_HEAD + '\n' + bookCSV(S.book), 'the current book');
      else if (t.id === 'cecsvall') copy(S.watch.length ? CSV_HEAD + '\n' + S.watch.map(bookCSV).filter(Boolean).join('\n') : '', 'the watchlist');
      else if (d.load != null) {
        const w = S.watch[+d.load];
        S.book = { want: w.want, have: w.have, league: w.league || '', avail: w.avail.map(r => Object.assign({}, r)), comp: w.comp.map(r => Object.assign({}, r)) };
        S.fph = w.fph ?? ''; save(); show(); msg(`Loaded ${w.want} / ${w.have} from ${w.date}.`);
      } else if (d.wdel != null) { S.watch.splice(+d.wdel, 1); save(); watch(); }
    };
  }

  return { show, parseRatio, parseRows, bestOf, spread, midpoint, label, flipOrders, depth, crossRate, analyse, rankWatch, toCSV,
           CSV_HEAD, TIGHT: CE_TIGHT, THIN: CE_THIN, TICK: CE_TICK, STOCK_UNIT: CE_STOCK_UNIT };
})();
if (typeof window !== 'undefined') window.CE = CE;
if (typeof module !== 'undefined' && module.exports) module.exports = CE;
