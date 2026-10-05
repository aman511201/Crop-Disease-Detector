/**
 * AgroScan AI Service Worker
 * Caches core app shell assets for instant startup and offline accessibility
 */

const CACHE_NAME = "agrosan-ai-v1";
const STATIC_ASSETS = [
    "/",
    "/static/css/style.css",
    "/static/js/main.js",
    "/static/manifest.json",
    "/static/icons/icon-192.png",
    "/static/icons/icon-512.png",
    "/static/favicon.ico"
];

// Install event - precache static shell
self.addEventListener("install", (event) => {
    event.waitUntil(
        caches.open(CACHE_NAME).then((cache) => {
            return cache.addAll(STATIC_ASSETS);
        }).then(() => self.skipWaiting())
    );
});

// Activate event - clean obsolete caches
self.addEventListener("activate", (event) => {
    event.waitUntil(
        caches.keys().then((keys) => {
            return Promise.all(
                keys.map((key) => {
                    if (key !== CACHE_NAME) {
                        return caches.delete(key);
                    }
                })
            );
        }).then(() => self.clients.claim())
    );
});

// Fetch event - Stale-while-revalidate for static assets, network-only for /api/predict
self.addEventListener("fetch", (event) => {
    const url = new URL(event.request.url);

    // Dynamic API prediction requests always use network
    if (url.pathname.startsWith("/api/predict")) {
        event.respondWith(fetch(event.request));
        return;
    }

    // App shell & static assets
    event.respondWith(
        caches.match(event.request).then((cachedResponse) => {
            if (cachedResponse) {
                // Fetch in background to update cache
                fetch(event.request).then((networkResponse) => {
                    if (networkResponse && networkResponse.status === 200) {
                        caches.open(CACHE_NAME).then((cache) => {
                            cache.put(event.request, networkResponse);
                        });
                    }
                }).catch(() => {});
                return cachedResponse;
            }
            return fetch(event.request);
        })
    );
});
