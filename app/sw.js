/* Offline support: app shell cached up front; data files served from cache and refreshed in the background. */
const VERSION = 'codex-v1';
const SHELL = ['./', 'index.html', 'db.js', 'exchange.js', 'manifest.webmanifest', 'icon.svg', 'icon-192.png', 'icon-512.png', 'kb.json', 'data/mods/index.json'];

self.addEventListener('install', e => {
  e.waitUntil(caches.open(VERSION).then(c => Promise.all(SHELL.map(u => c.add(u).catch(() => {})))).then(() => self.skipWaiting()));
});
self.addEventListener('activate', e => {
  e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== VERSION).map(k => caches.delete(k)))).then(() => self.clients.claim()));
});
self.addEventListener('fetch', e => {
  const url = new URL(e.request.url);
  if (e.request.method !== 'GET' || url.origin !== location.origin) return;
  // stale-while-revalidate: instant from cache, update behind the scenes
  e.respondWith(caches.open(VERSION).then(async c => {
    const hit = await c.match(e.request, { ignoreSearch: true });
    const net = fetch(e.request).then(r => { if (r.ok) c.put(e.request, r.clone()); return r; }).catch(() => hit);
    return hit || net;
  }));
});
