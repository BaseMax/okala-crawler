import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ── Directories ──────────────────────────────────────────────────────────────
CACHE_DIR   = os.path.join(BASE_DIR, "cache")
HTML_CACHE  = os.path.join(CACHE_DIR, "html")
JSON_CACHE  = os.path.join(CACHE_DIR, "json")
LOG_DIR     = os.path.join(BASE_DIR, "logs")
OUTPUT_DIR  = os.path.join(BASE_DIR, "outputs")

# ── HTTP client ───────────────────────────────────────────────────────────────
TIMEOUT         = 60        # seconds per request
MAX_RETRIES     = 5         # urllib3-level retries on 429/5xx
BACKOFF_FACTOR  = 2.0       # exponential back-off multiplier
VERIFY_SSL      = False     # disable SSL certificate verification
REQUEST_DELAY   = 0.5       # minimum seconds between outgoing requests

# ── Cache ─────────────────────────────────────────────────────────────────────
# TTL in seconds; set to 0 to cache forever (never expire)
CACHE_TTL = 86400   # 24 hours

# ── API ───────────────────────────────────────────────────────────────────────
API_BASE = "https://apigateway.okala.com"

# Coordinates used for nearby-stores queries (Tehran – Darakeh area)
LAT = 35.805851
LON = 51.431311

# Set to True to fetch full product detail (PDP) for every product.
# WARNING: this multiplies requests by the number of products per category.
FETCH_PRODUCT_DETAILS = False
