import hashlib
import json
import os
import tempfile
import time
from typing import Any, Optional

from config import CACHE_TTL, HTML_CACHE, JSON_CACHE
from core.logger import get_logger

logger = get_logger("cache")

class CacheManager:
    def __init__(self, ttl: int = CACHE_TTL) -> None:
        self.ttl = ttl
        os.makedirs(HTML_CACHE, exist_ok=True)
        os.makedirs(JSON_CACHE, exist_ok=True)

    @staticmethod
    def _key(url: str) -> str:
        return hashlib.md5(url.encode("utf-8")).hexdigest()

    def _json_path(self, key: str) -> str:
        return os.path.join(JSON_CACHE, f"{key}.json")

    def _meta_path(self, key: str) -> str:
        return os.path.join(JSON_CACHE, f"{key}.meta.json")

    def _html_path(self, url: str) -> str:
        return os.path.join(HTML_CACHE, f"{self._key(url)}.html")

    def _expired(self, meta_path: str) -> bool:
        """Return True if the cached entry is past its TTL."""
        if self.ttl == 0:
            return False
        if not os.path.exists(meta_path):
            return True
        try:
            with open(meta_path, "r", encoding="utf-8") as f:
                meta = json.load(f)
            return time.time() > meta.get("expires_at", 0)
        except Exception:
            return True

    @staticmethod
    def _safe_remove(*paths: str) -> None:
        for path in paths:
            try:
                if os.path.exists(path):
                    os.remove(path)
            except OSError:
                pass

    @staticmethod
    def _atomic_write(path: str, content: str) -> None:
        dir_ = os.path.dirname(path)
        tmp_path: Optional[str] = None
        try:
            with tempfile.NamedTemporaryFile(
                "w", dir=dir_, encoding="utf-8", delete=False, suffix=".tmp"
            ) as tmp:
                tmp.write(content)
                tmp_path = tmp.name
            os.replace(tmp_path, path)
        except OSError as exc:
            if tmp_path and os.path.exists(tmp_path):
                os.remove(tmp_path)
            raise exc

    def get_json(self, url: str) -> Optional[Any]:
        key = self._key(url)
        data_path = self._json_path(key)
        meta_path = self._meta_path(key)

        if not os.path.exists(data_path):
            return None

        if self._expired(meta_path):
            logger.debug(f"Cache expired, evicting: {url}")
            self._safe_remove(data_path, meta_path)
            return None

        try:
            with open(data_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            logger.info(f"[CACHE HIT] {url}")
            return data
        except (json.JSONDecodeError, OSError) as exc:
            logger.warning(f"Corrupt cache entry for {url}: {exc} - evicting")
            self._safe_remove(data_path, meta_path)
            return None

    def save_json(self, url: str, data: Any) -> None:
        key = self._key(url)
        data_path = self._json_path(key)
        meta_path = self._meta_path(key)

        try:
            serialised = json.dumps(data, ensure_ascii=False, indent=2)
            self._atomic_write(data_path, serialised)

            meta = {
                "url":        url,
                "cached_at":  time.time(),
                "expires_at": time.time() + self.ttl if self.ttl > 0 else 0,
                "size_bytes": len(serialised.encode("utf-8")),
            }
            self._atomic_write(meta_path, json.dumps(meta, indent=2))
            logger.debug(f"Cached → {data_path}")
        except OSError as exc:
            logger.error(f"Failed to write JSON cache for {url}: {exc}")

    def get_html(self, url: str) -> Optional[str]:
        path = self._html_path(url)
        if not os.path.exists(path):
            return None
        try:
            with open(path, "r", encoding="utf-8") as f:
                return f.read()
        except OSError as exc:
            logger.warning(f"HTML cache read failed for {url}: {exc}")
            return None

    def save_html(self, url: str, content: str) -> None:
        path = self._html_path(url)
        try:
            self._atomic_write(path, content)
            logger.debug(f"Cached HTML → {path}")
        except OSError as exc:
            logger.error(f"Failed to write HTML cache for {url}: {exc}")

    def stats(self) -> dict:
        json_entries = sum(
            1 for f in os.listdir(JSON_CACHE)
            if f.endswith(".json") and not f.endswith(".meta.json")
        )
        html_entries = (
            sum(1 for f in os.listdir(HTML_CACHE) if f.endswith(".html"))
            if os.path.exists(HTML_CACHE)
            else 0
        )
        return {"json_entries": json_entries, "html_entries": html_entries}
