#!/usr/bin/env node
/* Tests for app/exchange.js pure functions. Fixtures: David's in-game books 2026-11-27
   (typed in the paste format, and read back from data/prices/2026-11-27_exchange-books.csv).
   Run: node tools/test_exchange.js   (prints failures only; exit 1 on any failure) */
const fs = require('fs'), path = require('path');
const CE = require(path.join(__dirname, '..', 'app', 'exchange.js'));
let fails = 0, n = 0;
const ok = (cond, msg) => { n++; if (!cond) { fails++; console.log('FAIL ' + msg); } };
const near = (a, b, tol, msg) => ok(Number.isFinite(a) && Math.abs(a - b) <= tol, `${msg}: got ${a}, want ${b} ±${tol}`);
const PP = 1e-4; // ±0.01 percentage point

const FIX = [
  { name: 'Scroll of Wisdom / Exalted Orb',
    avail: '22 : 1   12,187\n20 : 1 5,526\n18.50 : 1 35,890\n15 6525\n3.05 : 1 61\n< 3.05 : 1 139',
    comp: '22.50 : 1 59\n150 : 1 1,221',
    a: 22, c: 22.5, spread: 0.022727, label: 'tight', buyR: 22.49, sellR: 22.01, margin: 22.49 / 22.01 - 1 },
  { name: 'Orb of Augmentation / Exalted Orb',
    avail: '2.30 : 1 175\n2.20 : 1 167\n1.65 : 1 200\n1.61 : 1 1,771\n1.60 : 1 56\n< 1.60 : 1 17,313',
    comp: '19 : 1 11\n20 : 1 49\n50 : 1 5\n1000 : 1 2',
    a: 2.3, c: 19, spread: 19 / 2.3 - 1, label: 'illiquid', buyR: 18.99, sellR: 2.31, margin: 18.99 / 2.31 - 1 },
  { name: 'Regal Orb / Exalted Orb',
    avail: '1.11 : 1 1,769\n1 : 1 74\n1 : 3 20',
    comp: '2.28 : 1 981\n2.29 : 1 1,000\n2.30 : 1 521\n2.40 : 1 135\n2.60 : 1 193\n> 2.60 : 1 6,004',
    a: 1.11, c: 2.28, spread: 2.28 / 1.11 - 1, label: 'illiquid', buyR: 2.27, sellR: 1.12, margin: 2.27 / 1.12 - 1 },
];

function check(name, avail, comp, f) {
  const A = CE.analyse({ avail, comp });
  near(A.a && A.a.r, f.a, 1e-9, `${name} best available`);
  near(A.c && A.c.r, f.c, 1e-9, `${name} best competing`);
  near(A.spread, f.spread, PP, `${name} spread`);
  ok(A.label === f.label, `${name} label: got ${A.label}, want ${f.label}`);
  ok(A.flip && A.flip.room, `${name} has room`);
  near(A.flip.buyR, f.buyR, 1e-9, `${name} buyR`);
  near(A.flip.sellR, f.sellR, 1e-9, `${name} sellR`);
  near(A.flip.margin, f.margin, PP, `${name} margin`);
}

// 1. fixtures typed in paste format
for (const f of FIX) {
  const pa = CE.parseRows(f.avail), pc = CE.parseRows(f.comp);
  ok(!pa.junk.length && !pc.junk.length, `${f.name}: paste had junk ${pa.junk.concat(pc.junk)}`);
  check(f.name + ' (paste)', pa.rows, pc.rows, f);
}
// expected headline numbers from the kickoff
near(CE.analyse({ avail: CE.parseRows(FIX[0].avail).rows, comp: CE.parseRows(FIX[0].comp).rows }).flip.margin, 0.0218, 0.0001, 'scroll margin ≈ 2.18%');
near(FIX[1].spread, 7.26, 0.001, 'aug spread ≈ 726%');
near(FIX[1].margin, 7.22, 0.001, 'aug margin ≈ 722%');
near(FIX[2].spread, 1.054, 0.0001, 'regal spread ≈ 105.4%');
near(FIX[2].margin, 1.027, 0.0005, 'regal margin ≈ 102.7% (kickoff figure is rounded)');

// 2. same fixtures read from the repo CSV
const csvPath = path.join(__dirname, '..', 'data', 'prices', '2026-11-27_exchange-books.csv');
if (fs.existsSync(csvPath)) {
  const lines = fs.readFileSync(csvPath, 'utf8').trim().split(/\r?\n/).slice(1);
  const books = {};
  for (const l of lines) {
    const c = l.split(','), key = c[2] + ' / ' + c[3], p = CE.parseRatio(c[5]);
    ok(p, `CSV ratio parses: ${c[5]}`);
    (books[key] = books[key] || { avail: [], comp: [] })[c[4] === 'available' ? 'avail' : 'comp'].push(Object.assign(p || {}, { stock: +c[6] }));
  }
  for (const f of FIX) { ok(books[f.name], `CSV has ${f.name}`); if (books[f.name]) check(f.name + ' (csv)', books[f.name].avail, books[f.name].comp, f); }
} else ok(false, 'missing ' + csvPath);

// 3. parsing edge cases
const r13 = CE.parseRatio('1 : 3');
near(r13 && r13.r, 1 / 3, 1e-12, '1 : 3 = 0.333');
ok(r13 && r13.text === '1:3', '1 : 3 keeps text 1:3');
ok(CE.parseRatio('< 3.05 : 1').tail === '<' && CE.parseRatio('>2.60').tail === '>', 'tail markers');
const pr = CE.parseRows('22 12187\n22 : 1\t12,187\nfoo bar\n0 : 1 5\n: 1 5\n22 : 0 5\n1,234,567 : 1 1\n\n');
ok(pr.rows.length === 3, `rows parsed: ${pr.rows.length}`);
ok(pr.junk.length === 4, `junk kept out: ${pr.junk.length}`);
ok(pr.rows[1].stock === 12187, 'comma stock');
ok(pr.rows[2].r === 1234567, 'comma ratio');
ok(CE.bestOf(CE.parseRows('< 50 : 1 9\n10 : 1 1').rows, 'available').r === 10, 'tail never best (available)');
ok(CE.bestOf(CE.parseRows('> 1 : 1 9\n10 : 1 1').rows, 'competing').r === 10, 'tail never best (competing)');
ok(CE.bestOf(CE.parseRows('< 3 : 1 9').rows, 'available') === null, 'only tails → no best');
ok(CE.analyse({ avail: [{ r: NaN, text: 'x' }], comp: [{ r: 5 }] }).spread === undefined, 'junk row never best');

// 4. no room, labels, thresholds
ok(!CE.flipOrders(22, 22.02, 0.01).room, 'no room at 2 ticks');
ok(CE.flipOrders(22, 22.03, 0.01).room, 'room at 3 ticks');
ok(CE.label(0.0499) === 'tight' && CE.label(0.05) === 'thin' && CE.label(0.5) === 'thin' && CE.label(0.51) === 'illiquid', 'label cut-offs');
ok(CE.TIGHT === 0.05 && CE.THIN === 0.5 && CE.TICK === 0.01 && CE.STOCK_UNIT === 'X', 'default constants');
near(CE.midpoint(22, 22.5), Math.sqrt(495), 1e-12, 'midpoint');

// 5. depth
const sa = CE.parseRows(FIX[0].avail).rows;
let d = CE.depth(sa, 13000, 'available');
near(d.filled, 13000, 1e-9, 'depth fills 13000');
near(d.y, 12187 / 22 + 813 / 20, 1e-6, 'depth cost walks rows');
ok(!d.partial && !d.approx, 'depth flags clean');
d = CE.depth(sa, 1e9, 'available');
ok(d.partial && d.approx, 'depth partial + uses tail');
const sc = CE.parseRows(FIX[0].comp).rows;
d = CE.depth(sc, 100, 'competing', 'X');
near(d.y, 59 / 22.5 + 41 / 150, 1e-7, 'instant sell, stock in X');
d = CE.depth(sc, 100, 'competing', 'Y');
near(d.y, 100 / 22.5, 1e-7, 'instant sell, stock in Y (59 Y covers 1327 X)');

// 6. cross rate (KB example: 140 ex, 6.25 chaos, 28 ex per chaos → +25% on cost)
const x = CE.crossRate(140, 6.25, 28);
near(x.aToB, 0.25, 1e-12, 'trinity +25%');
near(x.bToA, -0.2, 1e-12, 'trinity reverse −20%');
ok(CE.crossRate(0, 1, 1) === null, 'cross rate rejects zero');

// 7. ranking + CSV
const rk = CE.rankWatch([{ want: 'a', margin: 7, fph: '' }, { want: 'b', margin: 0.02, fph: 30 }, { want: 'c', margin: 1, fph: 0.1 }]);
ok(rk.map(w => w.want).join('') === 'bca', `rank order ${rk.map(w => w.want).join('')}`);
const csv = CE.toCSV({ date: '2026-11-27', league: 'Forbidden Rites', want: 'Regal Orb', have: 'Exalted Orb',
  avail: CE.parseRows(FIX[2].avail).rows, comp: CE.parseRows('> 2.60 : 1 6,004').rows }).split('\n');
ok(csv.length === 4, 'csv rows');
ok(csv[0] === '2026-11-27,Forbidden Rites,Regal Orb,Exalted Orb,available,1.11,1769', 'csv row 1: ' + csv[0]);
ok(csv[2].endsWith('available,1:3,20'), 'csv 1:3: ' + csv[2]);
ok(csv[3].endsWith('competing,>2.60,6004'), 'csv tail: ' + csv[3]);
ok(CE.CSV_HEAD === 'date,league,want,have,side,ratio_want_per_have,stock', 'csv header');
ok(CE.toCSV({ date: 'd', league: 'a,b', want: 'w', have: 'h', avail: [{ r: 2, text: '2', stock: 1 }], comp: [] }).startsWith('d,"a,b",'), 'csv quoting');

if (fails) { console.log(`${fails}/${n} failed`); process.exit(1); }
