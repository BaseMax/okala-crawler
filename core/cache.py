import os
import hashlib
import json
from config import HTML_CACHE, JSON_CACHE

class CacheManager:
    def __init__(self):
        os.makedirs(HTML_CACHE, exist_ok=True)
        os.makedirs(JSON_CACHE, exist_ok=True)

    def _hash(self, key: str):
        return hashlib.md5(key.encode()).hexdigest()

    def html_path(self, url):
        return os.path.join(HTML_CACHE, self._hash(url) + ".html")

    def json_path(self, key):
        return os.path.join(JSON_CACHE, self._hash(key) + ".json")

    # -------- HTML CACHE -------- #
    def get_html(self, url):
        path = self.html_path(url)
        if os.path.exists(path):
            return open(path, "r", encoding="utf-8").read()
        return None

    def save_html(self, url, content):
        path = self.html_path(url)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

    # -------- JSON CACHE -------- #
    def get_json(self, key):
        path = self.json_path(key)
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        return None

    def save_json(self, key, data):
        path = self.json_path(key)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)