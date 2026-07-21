const CACHE_NAME = 'crypto-analyzer-v1';
const ASSETS = [
  '/Cryptocurrency-Analyzer/',
  '/Cryptocurrency-Analyzer/index.html',
  '/Cryptocurrency-Analyzer/manifest.json',
  '/Cryptocurrency-Analyzer/icon-192.png',
  '/Cryptocurrency-Analyzer/icon-512.png',
  '/Cryptocurrency-Analyzer/sw.js'
];

self.addEventListener('install', (e) => {
  e.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      return cache.addAll(ASSETS.map(url => new URL(url, self.location.origin).href));
    })
  );
  self.skipWaiting();
});

self.addEventListener('fetch', (e) => {
  e.respondWith(
    caches.match(e.request).then((response) => {
      return response || fetch(e.request);
    })
  );
});

self.addEventListener('activate', (e) => {
  e.waitUntil(self.clients.claim());
});
