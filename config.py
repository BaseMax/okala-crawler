# config.py
import os

BASE_DIR = os.path.dirname(__file__)

CACHE_DIR = os.path.join(BASE_DIR, "cache")
HTML_CACHE = os.path.join(CACHE_DIR, "html")
JSON_CACHE = os.path.join(CACHE_DIR, "json")
LOG_DIR = os.path.join(BASE_DIR, "logs")

OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")

TIMEOUT = 30
MAX_RETRIES = 5
BACKOFF_FACTOR = 1.5

VERIFY_SSL = False
