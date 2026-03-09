// 에너지 OS — Service Worker v1.0
const CACHE_NAME = 'energy-os-v1';
const OFFLINE_URL = 'offline.html';

const FILES_TO_CACHE = [
  'manifest.json',
  'offline.html',
  'day01_energy_systems.html',
  'day02_mitochondria.html',
  'day03_hormones.html',
  'day04_autonomic.html',
  'day05_review.html',
  'day06_sleep_architecture.html',
  'day07_sleep_hormones.html',
  'day08_sleep_environment.html',
  'day09_sleep_debt.html',
  'day10_sleep_tracking.html',
  'day11_nutrition_basics.html',
  'day12_protein.html',
  'day13_carbs.html',
  'day14_fats_micros.html',
  'day15_hydration_caffeine.html',
  'day16_meal_timing.html',
  'day17_nutrition_review.html',
  'day18_hypertrophy_science.html',
  'day19_big_three.html',
  'day20_upper_body.html',
  'day21_lower_core.html',
  'day22_periodization.html',
  'day23_injury_mobility.html',
  'day24_recovery.html',
  'day25_weight_review.html',
  'day26_vo2max_lactate.html',
  'day27_running_form.html',
  'day28_interval_training.html',
  'day29_zone_training.html',
  'day30_concurrent_training.html',
  'day31_running_review.html',
  'day32_hrv.html',
  'day33_immune_energy.html',
  'day34_fatigue_overtraining.html',
  'day35_travel_seasonal.html',
  'day36_condition_review.html',
  'day37_morning_routine.html',
  'day38_evening_routine.html',
  'day39_weekend_routine.html',
  'day40_routine_review.html',
  'day41_stress_neuroscience.html',
  'day42_meditation_breathwork.html',
  'day43_flow_state.html',
  'day44_emotional_regulation.html',
  'day45_mental_review.html',
  'day46_biohacking_tech.html',
  'day47_supplementation.html',
  'day48_social_energy.html',
  'day49_digital_detox.html',
  'day50_final_integration.html'
];

// Install: pre-cache all files
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => {
      console.log('[SW] Pre-caching all 50 days');
      return cache.addAll(FILES_TO_CACHE);
    }).then(() => self.skipWaiting())
  );
});

// Activate: clean old caches
self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(keys => {
      return Promise.all(
        keys.filter(k => k !== CACHE_NAME).map(k => caches.delete(k))
      );
    }).then(() => self.clients.claim())
  );
});

// Fetch: cache-first, network fallback, offline page last resort
self.addEventListener('fetch', event => {
  // Only handle same-origin GET requests
  if (event.request.method !== 'GET') return;

  // For Google Fonts: network-first with cache fallback
  if (event.request.url.includes('fonts.googleapis.com') ||
      event.request.url.includes('fonts.gstatic.com')) {
    event.respondWith(
      fetch(event.request).then(response => {
        const clone = response.clone();
        caches.open(CACHE_NAME).then(cache => cache.put(event.request, clone));
        return response;
      }).catch(() => caches.match(event.request))
    );
    return;
  }

  // For HTML files: cache-first, then network
  event.respondWith(
    caches.match(event.request).then(cached => {
      if (cached) {
        // Return cache immediately, update in background
        fetch(event.request).then(response => {
          caches.open(CACHE_NAME).then(cache => cache.put(event.request, response));
        }).catch(() => {});
        return cached;
      }
      // Not in cache: try network, fallback to offline page
      return fetch(event.request).then(response => {
        const clone = response.clone();
        caches.open(CACHE_NAME).then(cache => cache.put(event.request, clone));
        return response;
      }).catch(() => {
        if (event.request.destination === 'document') {
          return caches.match(OFFLINE_URL);
        }
      });
    })
  );
});
