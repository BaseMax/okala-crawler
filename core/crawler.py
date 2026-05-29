from core.client import HTTPClient
from core.cache import CacheManager
from core.pipeline import DataPipeline
from core.logger import get_logger

import json

logger = get_logger("crawler")

class OkalaCrawler:
    def __init__(self):
        self.client = HTTPClient()
        self.cache = CacheManager()
        self.pipeline = DataPipeline()

    # -------- CATEGORY PRODUCTS -------- #
    def fetch_category_products(self, url, headers):
        cached = self.cache.get_json(url)
        if cached:
            logger.info(f"[CACHE HIT] {url}")
            return cached

        response = self.client.get(url, headers=headers)
        if not response:
            return None

        data = response.json()

        self.cache.save_json(url, data)
        return data

    # -------- STORE → CATEGORY -------- #
    def crawl_store_category(self, store_id, category_slug, category_id, headers):
        url = f"https://apigateway.okala.com/api/unicorn/v2/products/store/{store_id}?pC_Id={category_id}&slug={category_slug}"

        data = self.fetch_category_products(url, headers)
        if not data:
            return None

        products = data.get("data", [])

        return {
            "store_id": store_id,
            "category": category_slug,
            "products": products
        }

    # -------- NEARBY STORES -------- #
    def crawl_nearby_stores(self, url, headers):
        cached = self.cache.get_json(url)
        if cached:
            return cached

        response = self.client.get(url, headers=headers)
        if not response:
            return None

        data = response.json()
        self.cache.save_json(url, data)
        return data