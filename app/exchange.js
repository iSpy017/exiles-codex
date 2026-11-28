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
  // Layout: pair → two best ratios → verdict + ladder → the two orders to place → profit → optional depth/settings.
  const KEY = 'codex-ce2';
  const CURRENCIES = ['Exalted Orb', 'Divine Orb', 'Chaos Orb', 'Scroll of Wisdom', 'Orb of Augmentation', 'Regal Orb', 'Orb of Annulment',
    'Orb of Chance', 'Greater Chaos Orb', 'Greater Exalted Orb', 'Greater Regal Orb', 'Perfect Chaos Orb', 'Perfect Exalted Orb',
    'Perfect Orb of Augmentation', "Perfect Jeweller's Orb", 'Fracturing Orb', 'Vaal Orb', "Architect's Orb", "Armourer's Scrap",
    "Blacksmith's Whetstone", 'Mirror of Kalandra']; // names from data/prices (Runes of Aldur + 2026-11-27 books)
  // David's in-game books, 2026-11-27 (data/prices/2026-11-27_exchange-books.csv)
  const EXAMPLES = [
    { label: 'Scrolls', want: 'Scroll of Wisdom', have: 'Exalted Orb', avail: '22 : 1  12,187\n20 : 1  5,526\n18.50 : 1  35,890\n15 : 1  6,525\n3.05 : 1  61\n< 3.05 : 1  139', comp: '22.50 : 1  59\n150 : 1  1,221' },
    { label: 'Augmentations', want: 'Orb of Augmentation', have: 'Exalted Orb', avail: '2.30 : 1  175\n2.20 : 1  167\n1.65 : 1  200\n1.61 : 1  1,771\n1.60 : 1  56\n< 1.60 : 1  17,313', comp: '19 : 1  11\n20 : 1  49\n50 : 1  5\n1000 : 1  2' },
    { label: 'Regals', want: 'Regal Orb', have: 'Exalted Orb', avail: '1.11 : 1  1,769\n1 : 1  74\n1 : 3  20', comp: '2.28 : 1  981\n2.29 : 1  1,000\n2.30 : 1  521\n2.40 : 1  135\n2.60 : 1  193\n> 2.60 : 1  6,004' },
  ];
  const today = () => { const d = new Date(); return new Date(d - d.getTimezoneOffset() * 6e4).toISOString().slice(0, 10); };
  let S = { tab: 'flip', want: '', have: '', ba: '', bc: '', availText: '', compText: '', league: 'Forbidden Rites',
            tick: CE_TICK, unit: CE_STOCK_UNIT, tight: CE_TIGHT * 100, thin: CE_THIN * 100, stake: '100', n: '', fph: '',
            cross: { pA: '', a: 'Exalted Orb', pB: '', b: 'Chaos Orb', rate: '' }, watch: [] };
  try {
    if (typeof localStorage !== 'undefined') {
      const saved = JSON.parse(localStorage.getItem(KEY) || 'null');
      if (saved) S = Object.assign(S, saved);
      else { const old = JSON.parse(localStorage.getItem('codex-ce') || '{}'); if (Array.isArray(old.watch)) S.watch = old.watch; }
    }
  } catch (e) {}
  const save = () => { try { localStorage.setItem(KEY, JSON.stringify(S)); } catch (e) {} };
  const $ = id => document.getElementById(id);
  const fR = x => Number.isFinite(x) ? String(clean(Math.round(x * 1e4) / 1e4)) : '—';
  const fP = x => Number.isFinite(x) ? (Math.abs(x) >= 10 ? (x * 100).toFixed(0) : (x * 100).toFixed(2)) + '%' : '—';
  const fN = x => Number.isFinite(x) ? (Math.abs(x) >= 100 ? Math.round(x).toLocaleString('en') : String(Math.round(x * 100) / 100)) : '—';
  const fPrice = x => Number.isFinite(x) ? String(+x.toPrecision(4)) : '—';
  const opts = () => ({ tick: +S.tick || CE_TICK, tight: (+S.tight || CE_TIGHT * 100) / 100, thin: (+S.thin || CE_THIN * 100) / 100 });
  const X = () => E(S.want || 'the item'), Y = () => E(S.have || 'your currency');
  const Xs = () => E(S.want || 'X'), Ys = () => E(S.have || 'Y');
  const rowsOf = k => parseRows(S[k + 'Text']).rows;
  const bestRatio = s => { const p = parseRatio(s); return p && !p.tail ? p.r : NaN; };
  /** Book used for analysis: the two best-ratio fields (filled from the pasted book when there is one). */
  function current() {
    const a = bestRatio(S.ba), c = bestRatio(S.bc);
    const av = rowsOf('avail'), cp = rowsOf('comp');
    return { a, c, avail: av.length ? av : (a > 0 ? [{ r: a, text: S.ba.trim(), stock: null }] : []),
             comp: cp.length ? cp : (c > 0 ? [{ r: c, text: S.bc.trim(), stock: null }] : []), hasBook: !!(av.length && cp.length) };
  }

  function show() {
    const R = document.getElementById('reader');
    R.innerHTML = `<div class="ce">
      <h1>Exchange margin</h1>
      <p class="sub">Type the top ratio from each side of the in-game book. You get the two orders to place and what one round trip makes.</p>
      <div class="cetabs" role="tablist" aria-label="Exchange tools">
        <button role="tab" type="button" data-tab="flip" aria-selected="${S.tab === 'flip'}">Flip a pair</button>
        <button role="tab" type="button" data-tab="cross" aria-selected="${S.tab === 'cross'}">Cross-currency</button>
        <button role="tab" type="button" data-tab="watch" aria-selected="${S.tab === 'watch'}">Watchlist <span class="cnt" id="cewcount">${S.watch.length || ''}</span></button>
      </div>
      <div id="cepanel" role="tabpanel"></div>
      <datalist id="cecur">${CURRENCIES.map(c => `<option value="${E(c)}">`).join('')}</datalist>
      <p class="foot">How it works: <a href="#strategy-flipping-strats">flipping strategies</a> (undercut by the smallest step; judge by margin × how often it fills) and <a href="#economy-currency-exchange">Currency Exchange mechanics</a>. The page does arithmetic only; ratios, stock and fills per hour come from you. Everything is saved in this browser.</p>
    </div>`;
    bind(); panel();
  }

  function panel() {
    document.querySelectorAll('.cetabs [data-tab]').forEach(b => b.setAttribute('aria-selected', b.dataset.tab === S.tab));
    const P = $('cepanel');
    if (S.tab === 'cross') { P.innerHTML = crossHTML(); cross(); return; }
    if (S.tab === 'watch') { P.innerHTML = watchHTML(); return; }
    P.innerHTML = `
      <div class="cepair">
        <label class="cef"><span>I want</span><input id="cewant" list="cecur" value="${E(S.want)}" placeholder="Scroll of Wisdom" autocomplete="off"></label>
        <button type="button" class="ceswap" id="ceswap" aria-label="Swap want and have" title="Swap"><svg viewBox="0 0 24 24"><path d="M4 8h13l-3-3M20 16H7l3 3"/></svg></button>
        <label class="cef"><span>I have</span><input id="cehave" list="cecur" value="${E(S.have)}" placeholder="Exalted Orb" autocomplete="off"></label>
      </div>
      <div class="cebest">
        <label class="cef big"><span>Best Available</span><small>Top of the left list (highest ratio)</small>
          <span class="ratio"><input id="ceba" inputmode="decimal" value="${E(S.ba)}" placeholder="22" autocomplete="off"><i>: 1</i></span></label>
        <label class="cef big"><span>Best Competing</span><small>Top of the right list (lowest ratio)</small>
          <span class="ratio"><input id="cebc" inputmode="decimal" value="${E(S.bc)}" placeholder="22.5" autocomplete="off"><i>: 1</i></span></label>
      </div>
      <p class="ceex">No book open? Load one of the 27 Nov books: ${EXAMPLES.map((x, i) => `<button type="button" class="pill" data-ex="${i}">${x.label}</button>`).join('')}</p>
      <div id="ceout" aria-live="polite"></div>
      <details class="cemore" id="cebook"${S.availText || S.compText ? ' open' : ''}>
        <summary>Paste the whole book <small>for instant-fill depth and the CSV</small></summary>
        <div class="cebook">
          <label class="cef"><span>Available Trades</span><textarea id="ceat" rows="6" spellcheck="false" placeholder="22 : 1   12,187&#10;20 : 1   5,526&#10;&lt; 3.05 : 1   139">${E(S.availText)}</textarea><small id="ceas"></small></label>
          <label class="cef"><span>Competing Trades</span><textarea id="cect" rows="6" spellcheck="false" placeholder="22.50 : 1   59&#10;150 : 1   1,221">${E(S.compText)}</textarea><small id="cecs"></small></label>
        </div>
        <p class="cehint">One row per line: ratio then stock. Rows starting with &lt; or &gt; are the game's grouped tails; they count for depth but never as the best order. The best-ratio boxes above fill in from what you paste.</p>
        <div class="cerow"><label class="cef inline"><span>Instant fill</span><input id="cen" inputmode="decimal" value="${E(S.n)}" placeholder="1000"></label><span class="cehint">${Xs()} bought or sold right now against the book</span></div>
        <div id="cedepth"></div>
      </details>
      <details class="cemore">
        <summary>Assumptions <small>tick ${E(S.tick)}, stock in ${S.unit}, tight under ${E(S.tight)}%, illiquid over ${E(S.thin)}%</small></summary>
        <div class="cerow wrap">
          <label class="cef inline"><span>Tick (smallest ratio step)</span><input id="cetick" inputmode="decimal" value="${E(S.tick)}"></label>
          <label class="cef inline"><span>Competing “Stock” counts</span><select id="ceunit"><option value="X"${S.unit === 'X' ? ' selected' : ''}>the item wanted</option><option value="Y"${S.unit === 'Y' ? ' selected' : ''}>the currency offered</option></select></label>
          <label class="cef inline"><span>Tight below %</span><input id="cetight" inputmode="decimal" value="${E(S.tight)}"></label>
          <label class="cef inline"><span>Illiquid above %</span><input id="cethin" inputmode="decimal" value="${E(S.thin)}"></label>
        </div>
        <p class="cehint">None of these are confirmed game facts. The tick comes from the two-decimal ratios on screen and the creators' “undercut by 0.01”. Which unit Competing stock counts is unconfirmed. The gold order fee is left out because gold only costs time.</p>
      </details>`;
    bookStatus(); out();
  }

  function bookStatus() {
    for (const [k, id] of [['avail', 'ceas'], ['comp', 'cecs']]) {
      const el = $(id); if (!el) continue;
      const p = parseRows(S[k + 'Text']);
      el.textContent = !S[k + 'Text'].trim() ? '' : `${p.rows.length} row${p.rows.length === 1 ? '' : 's'} read` + (p.junk.length ? `; skipped: ${p.junk.slice(0, 2).join(' | ')}${p.junk.length > 2 ? ' …' : ''}` : '');
      el.className = p.junk.length ? 'bad' : '';
    }
  }

  const VERDICT = {
    tight: ['Tight spread: good to flip', s => `The book is only ${fP(s)} wide, so orders here fill often. Both of your orders sit first in line.`],
    thin: ['Thin book: slower fills', s => `A ${fP(s)} spread means fewer trades. Put in your fills per hour before you commit much.`],
    illiquid: ['Wide spread: few trades happen', s => `${fP(s)} apart because hardly anyone trades this pair. The margin only pays if someone fills both orders, so post and wait rather than plan around it.`],
    crossed: ['Check the ratios', () => 'Best Competing should be higher than Best Available. The two boxes may be swapped.'],
  };

  function ladder(a, c, f) {
    const pts = [{ r: a, t: `Sellers' best ${fR(a)}`, k: 'edge' }, { r: c, t: `Buyers' best ${fR(c)}`, k: 'edge' }];
    if (f.room) pts.push({ r: f.sellR, t: `You sell at ${fR(f.sellR)}`, k: 'you' }, { r: f.buyR, t: `You buy at ${fR(f.buyR)}`, k: 'you' });
    const lo = Math.log(a), hi = Math.log(c), pos = r => 8 + 84 * (Math.log(r) - lo) / (hi - lo || 1);
    return `<div class="ladder" role="img" aria-label="Sellers' best ${fR(a)}, buyers' best ${fR(c)} ${Xs()} per ${Ys()}${f.room ? `; your sell ${fR(f.sellR)}, your buy ${fR(f.buyR)}` : ''}">
      <div class="track"><div class="gap" style="left:${pos(a)}%;right:${100 - pos(c)}%"></div>
      ${pts.map((p, i) => `<span class="mk ${p.k} ${i % 2 ? 'r' : 'l'}" style="left:${pos(p.r)}%"><b></b><em>${p.t}</em></span>`).join('')}</div>
      <div class="axis"><span>more ${Xs()} per ${Ys()} is to the right</span></div></div>`;
  }

  function out() {
    const el = $('ceout'); if (!el) return;
    const o = opts(), cur = current();
    if (!(cur.a > 0) || !(cur.c > 0)) {
      el.innerHTML = `<div class="ceempty">${S.ba || S.bc ? 'Both best ratios are needed. Type them as shown in game, like 22 or 18.50 (or 1 : 3).' : 'Your margin, the two orders to place and what a round trip makes will show here.'}</div>`;
      const d = $('cedepth'); if (d) d.innerHTML = ''; return;
    }
    const s = spread(cur.a, cur.c), lab = label(s, o.tight, o.thin), f = flipOrders(cur.a, cur.c, o.tick);
    const [vt, vb] = VERDICT[lab] || VERDICT.crossed, stake = parseFloat(S.stake), fph = parseFloat(S.fph);
    let h = `<div class="verdict ${lab}${f.room ? '' : ' none'}">
      <div class="vm">${f.room ? `<span class="big">${fP(f.margin)}</span><span>per round trip</span>` : `<span class="big">None</span><span>no room to flip</span>`}</div>
      <div class="vt"><b>${f.room || lab === 'crossed' ? vt : 'No room to flip'}</b><p>${f.room || lab === 'crossed' ? vb(s) : `The best orders are within two ticks (${E(S.tick)} each), so undercutting both sides would cross the book.`}</p>
        <p class="vs">Spread ${fP(s)}. Mid price 1 ${Xs()} ≈ ${fPrice(1 / midpoint(cur.a, cur.c))} ${Ys()}.</p></div></div>`;
    if (lab !== 'crossed') h += ladder(cur.a, cur.c, f);
    if (f.room) {
      h += `<div class="slips">
        <div class="slip"><h3>Buy order</h3><p class="where">On the ${Xs()} / ${Ys()} pair</p>
          <dl><dt>I want</dt><dd>${X()}</dd><dt>I have</dt><dd>${Y()}</dd></dl>
          <div class="sr"><span class="rv">${fR(f.buyR)} : 1</span><button type="button" class="copy" data-copy="${fR(f.buyR)}">Copy ${fR(f.buyR)}</button></div>
          <p class="why">One tick below the best competing order, so you're first in line to buy.</p></div>
        <div class="slip"><h3>Sell order</h3><p class="where">On the reverse pair, ${Ys()} / ${Xs()}</p>
          <dl><dt>I want</dt><dd>${Y()}</dd><dt>I have</dt><dd>${X()}</dd></dl>
          <div class="sr"><span class="rv">1 : ${fR(f.sellR)}</span><button type="button" class="copy" data-copy="${fR(f.sellR)}">Copy ${fR(f.sellR)}</button></div>
          <p class="why">One tick above the best available order: ${fR(f.sellR)} ${Xs()} for each ${Ys()}.</p></div></div>
      <div class="profit">
        <label class="cef inline"><span>Cycle</span><input id="cestake" inputmode="decimal" value="${E(S.stake)}" placeholder="100"><i>${Ys()}</i></label>
        <p>${stake > 0 ? `Makes <b>+${fN(stake * f.margin)} ${Ys()}</b> per round trip, or keep <b>${fN(stake * (f.buyR - f.sellR))} ${Xs()}</b> instead.` : 'Enter an amount to see the profit per round trip.'}</p>
      </div>
      <div class="profit">
        <label class="cef inline"><span>Fills per hour</span><input id="cefph" inputmode="decimal" value="${E(S.fph)}" placeholder="your guess"></label>
        <p>${fph > 0 ? `About <b>${fP(f.margin * fph)}</b> of your stake per hour. Used to rank the watchlist.` : 'How often both orders fill, from watching the book. Ranks your watchlist.'}</p>
        <button type="button" class="cta" id="cesave">Save to watchlist</button>
      </div><p class="cemsg" id="cemsg" role="status"></p>`;
    }
    el.innerHTML = h;
    // depth (inside the book disclosure)
    const d = $('cedepth'), n = parseFloat(S.n);
    if (d) {
      if (!cur.hasBook) d.innerHTML = '<p class="cehint">Paste both sides above to see depth.</p>';
      else if (!(n > 0)) d.innerHTML = '';
      else {
        const d1 = depth(cur.avail, n, 'available'), d2 = depth(cur.comp, n, 'competing', S.unit);
        const note = x => (x.partial ? ` <span class="warn">Only ${fN(x.filled)} in the book.</span>` : '') + (x.approx ? ' <span class="cehint">Uses a grouped &lt;/&gt; row at its bound, so it is approximate.</span>' : '');
        d.innerHTML = `<div class="depth"><div><span>Buy ${fN(n)} ${Xs()} now</span><b>${d1.filled ? `${fN(d1.y)} ${Ys()}` : 'Nothing to fill'}</b><small>average ${fR(d1.avgR)} : 1${note(d1)}</small></div>
          <div><span>Sell ${fN(n)} ${Xs()} now</span><b>${d2.filled ? `${fN(d2.y)} ${Ys()}` : 'Nothing to fill'}</b><small>average ${fR(d2.avgR)} : 1${note(d2)}</small></div></div>`;
      }
    }
  }

  function crossHTML() {
    const c = S.cross;
    return `<p class="cehint lead">The same item priced in two currencies, plus the rate between those currencies. Shows the gain from buying in one and selling in the other, before fees.</p>
      <div class="xform">
        <p>One item costs <input id="cepa" inputmode="decimal" value="${E(c.pA)}" placeholder="140" aria-label="Price in currency A"> <input id="cea" class="cur" list="cecur" value="${E(c.a)}" aria-label="Currency A"></p>
        <p>or <input id="cepb" inputmode="decimal" value="${E(c.pB)}" placeholder="6.25" aria-label="Price in currency B"> <input id="ceb" class="cur" list="cecur" value="${E(c.b)}" aria-label="Currency B"></p>
        <p>and 1 <span id="cebn">${E(c.b || 'B')}</span> = <input id="cerate" inputmode="decimal" value="${E(c.rate)}" placeholder="28" aria-label="Rate"> <span id="cean">${E(c.a || 'A')}</span></p>
      </div>
      <div id="cecross" aria-live="polite"></div>
      <p class="ceex">Example from the flipping notes: <button type="button" class="pill" id="cexex">140 ex, 6.25 chaos, 28 ex per chaos</button></p>`;
  }
  function cross() {
    const c = S.cross, r = crossRate(+c.pA, +c.pB, +c.rate), el = $('cecross'); if (!el) return;
    const a = E(c.a || 'A'), b = E(c.b || 'B');
    if ($('cebn')) { $('cebn').textContent = c.b || 'B'; $('cean').textContent = c.a || 'A'; }
    if (!r) { el.innerHTML = '<div class="ceempty">Fill in both prices and the rate.</div>'; return; }
    const best = r.aToB >= r.bToA ? { g: r.aToB, buy: a, sell: b } : { g: r.bToA, buy: b, sell: a };
    el.innerHTML = `<div class="verdict ${best.g > 0 ? 'tight' : 'crossed'}"><div class="vm"><span class="big">${best.g > 0 ? '+' : ''}${fP(best.g)}</span><span>per lap</span></div>
      <div class="vt"><b>${best.g > 0 ? `Buy with ${best.buy}, sell for ${best.sell}` : 'No gain either way'}</b>
      <p>${fN(+c.pB)} ${b} is worth ${fN(c.pB * c.rate)} ${a}. Buying with ${a} and selling for ${b}: ${r.aToB >= 0 ? '+' : ''}${fP(r.aToB)}. The other way round: ${r.bToA >= 0 ? '+' : ''}${fP(r.bToA)}.</p></div></div>`;
  }

  function watchHTML() {
    const L = rankWatch(S.watch.map((w, i) => Object.assign({ i }, w)));
    const list = L.length ? `<ol class="wl">${L.map((w, k) => `<li class="${E(w.label || '')}">
        <span class="rk">${w.score == null ? '' : k + 1}</span>
        <div class="wn"><b>${E(w.want)}</b> <span>for ${E(w.have)}</span><small>saved ${E(w.date)}, spread ${fP(w.spread)} (${E(w.label || '')})</small></div>
        <div class="wv"><b>${w.margin == null ? 'No room' : fP(w.margin)}</b><small>${w.score == null ? (w.margin == null ? '' : 'add fills/hour to rank') : `${fP(w.score)} per hour`}</small></div>
        <div class="wa"><button type="button" class="pill" data-load="${w.i}">Open</button><button type="button" class="x" data-wdel="${w.i}" aria-label="Remove ${E(w.want)} for ${E(w.have)}">×</button></div></li>`).join('')}</ol>`
      : `<div class="ceempty">Nothing saved yet. Work out a pair under “Flip a pair”, then press Save to watchlist.</div>`;
    return `<p class="cehint lead">Pairs you've saved, best first by margin × fills per hour. Pairs without fills per hour go to the bottom.</p>${list}
      <div class="cerow wrap csv">
        <label class="cef inline"><span>League for the CSV</span><input id="celeague" value="${E(S.league)}"></label>
        <button type="button" class="pill" id="cecsvall"${S.watch.length ? '' : ' disabled'}>Copy watchlist as CSV</button>
        <button type="button" class="pill" id="cecsv">Copy current book as CSV</button>
      </div><p class="cehint">Rows match data/prices/*_exchange-books.csv, so a book can be added to the repo.</p><p class="cemsg" id="cemsg" role="status"></p>`;
  }

  function msg(t) { const m = $('cemsg'); if (m) m.textContent = t; }
  function copyText(text, done) {
    const fallback = () => { const t = document.createElement('textarea'); t.value = text; document.body.appendChild(t); t.select();
      try { document.execCommand('copy'); done(true); } catch (e) { done(false); } t.remove(); };
    if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(text).then(() => done(true), fallback); else fallback();
  }
  const bookCSV = bk => toCSV(Object.assign({ league: S.league }, bk, { date: bk.date || today() }));
  const curBookCSV = () => { const c = current(); return bookCSV({ want: S.want, have: S.have, avail: c.avail, comp: c.comp }); };

  function syncBest() { // pasted book → best boxes
    const a = bestOf(rowsOf('avail'), 'available'), c = bestOf(rowsOf('comp'), 'competing');
    if (a) { S.ba = a.text; if ($('ceba')) $('ceba').value = a.text; }
    if (c) { S.bc = c.text; if ($('cebc')) $('cebc').value = c.text; }
  }

  function bind() {
    const R = document.getElementById('reader');
    const map = { cewant: 'want', cehave: 'have', ceba: 'ba', cebc: 'bc', cestake: 'stake', cefph: 'fph', cen: 'n', celeague: 'league',
                  cetick: 'tick', ceunit: 'unit', cetight: 'tight', cethin: 'thin' };
    const cx = { cepa: 'pA', cea: 'a', cepb: 'pB', ceb: 'b', cerate: 'rate' };
    R.oninput = R.onchange = e => {
      if (!document.querySelector('.ce')) return;
      const t = e.target, id = t.id;
      if (cx[id]) { S.cross[cx[id]] = t.value; save(); cross(); return; }
      if (id === 'ceat' || id === 'cect') { S[id === 'ceat' ? 'availText' : 'compText'] = t.value; syncBest(); bookStatus(); }
      else if (map[id]) S[map[id]] = t.value; else return;
      save();
      if (id === 'cestake' || id === 'cefph') { refreshProfit(); return; }
      if (e.type === 'input' || id === 'ceunit') out();
    };
    R.onclick = e => {
      if (!document.querySelector('.ce')) return;
      const t = e.target.closest('button'); if (!t) return;
      const d = t.dataset;
      if (d.tab) { S.tab = d.tab; save(); panel(); return; }
      if (t.id === 'ceswap') { [S.want, S.have] = [S.have, S.want]; save(); panel(); return; }
      if (d.ex != null) { const x = EXAMPLES[+d.ex]; Object.assign(S, { want: x.want, have: x.have, availText: x.avail, compText: x.comp }); syncBest(); save(); panel(); return; }
      if (d.copy) { copyText(d.copy, ok => { const old = t.textContent; t.textContent = ok ? 'Copied' : 'Copy failed'; t.classList.add('done'); setTimeout(() => { t.textContent = old; t.classList.remove('done'); }, 1400); }); return; }
      if (t.id === 'cexex') { Object.assign(S.cross, { pA: '140', a: 'Exalted Orb', pB: '6.25', b: 'Chaos Orb', rate: '28' }); save(); panel(); return; }
      if (t.id === 'cesave') {
        const c = current(), o = opts(), f = flipOrders(c.a, c.c, o.tick), s = spread(c.a, c.c);
        const w = { want: S.want || 'X', have: S.have || 'Y', league: S.league, date: today(), fph: S.fph, spread: s, label: label(s, o.tight, o.thin),
                    margin: f.room ? f.margin : null, ba: S.ba, bc: S.bc, availText: S.availText, compText: S.compText, avail: c.avail, comp: c.comp };
        const j = S.watch.findIndex(x => x.want === w.want && x.have === w.have);
        if (j >= 0) S.watch[j] = w; else S.watch.push(w);
        save(); $('cewcount').textContent = S.watch.length; msg(`Saved ${w.want} for ${w.have}. It's on the Watchlist tab.`); return;
      }
      if (d.load != null) {
        const w = S.watch[+d.load];
        Object.assign(S, { tab: 'flip', want: w.want, have: w.have, fph: w.fph ?? '',
          ba: w.ba ?? (bestOf(w.avail, 'available') || {}).text ?? '', bc: w.bc ?? (bestOf(w.comp, 'competing') || {}).text ?? '',
          availText: w.availText ?? '', compText: w.compText ?? '' });
        save(); panel(); return;
      }
      if (d.wdel != null) { S.watch.splice(+d.wdel, 1); save(); $('cewcount').textContent = S.watch.length || ''; panel(); return; }
      if (t.id === 'cecsv' || t.id === 'cecsvall') {
        const body = t.id === 'cecsv' ? curBookCSV() : S.watch.map(bookCSV).filter(Boolean).join('\n');
        if (!body) { msg('Nothing to copy yet: the current book is empty.'); return; }
        copyText(CSV_HEAD + '\n' + body, ok => msg(ok ? `Copied ${body.split('\n').length} rows plus the header.` : 'Copy failed. Your browser blocked the clipboard.'));
      }
    };
  }
  // update only the profit sentences so the input being typed in keeps focus
  function refreshProfit() {
    const a = document.activeElement, id = a && a.id, pos = a && a.selectionStart;
    out();
    if (id && $(id)) { $(id).focus(); try { $(id).setSelectionRange(pos, pos); } catch (e) {} }
  }
  return { show, parseRatio, parseRows, bestOf, spread, midpoint, label, flipOrders, depth, crossRate, analyse, rankWatch, toCSV,
           CSV_HEAD, TIGHT: CE_TIGHT, THIN: CE_THIN, TICK: CE_TICK, STOCK_UNIT: CE_STOCK_UNIT };
})();
if (typeof window !== 'undefined') window.CE = CE;
if (typeof module !== 'undefined' && module.exports) module.exports = CE;
