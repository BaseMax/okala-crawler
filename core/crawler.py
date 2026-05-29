import sys
import json
from typing import Any, Dict, List, Optional

from config import API_BASE, FETCH_PRODUCT_DETAILS
from core.cache import CacheManager
from core.client import HTTPClient
from core.logger import get_logger

logger = get_logger("crawler")

class OkalaCrawler:
    def __init__(self, headers: Dict[str, str]) -> None:
        self.headers = headers
        self.client  = HTTPClient()
        self.cache   = CacheManager()

    def _fetch(self, url: str) -> Optional[Any]:
        cached = self.cache.get_json(url)
        if cached is not None:
            return cached

        response = self.client.get(url, headers=self.headers)
        if response is None:
            return None

        try:
            data = response.json()
        except (json.JSONDecodeError, ValueError) as exc:
            logger.error(f"Invalid JSON from {url}: {exc}")
            return None

        self.cache.save_json(url, data)
        return data

    def crawl_store_category(
        self, store_id: int, slug: str, category_id: int
    ) -> Optional[Dict]:
        url = (
            f"{API_BASE}/api/unicorn/v2/products/store/{store_id}"
            f"?pC_Id={category_id}&slug={slug}"
        )
        logger.info(f"Fetching store={store_id} category={slug}")

        data = self._fetch(url)
        if data is None:
            logger.warning(f"No data returned for store={store_id} category={slug}")
            return None

        products: List[Dict] = data.get("data") or []

        if not products:
            logger.warning(f"Empty product list for store={store_id} category={slug}")

        if FETCH_PRODUCT_DETAILS and products:
            products = self._enrich_products(store_id, products)

        return {
            "store_id":      store_id,
            "category_slug": slug,
            "category_id":   category_id,
            "product_count": len(products),
            "products":      products,
        }

    def fetch_product_detail(
        self, store_id: int, product_id: int
    ) -> Optional[Dict]:
        url = f"{API_BASE}/api/Unicorn/v1/catalog/pdp?sId={store_id}&pId={product_id}"
        logger.debug(f"Fetching PDP store={store_id} product={product_id}")
        return self._fetch(url)

    def crawl_nearby(
        self, slug: str, lat: float, lon: float
    ) -> Optional[Any]:
        url = f"{API_BASE}/api/unicorn/v2/products/nearby?slug={slug}&lat={lat}&lon={lon}"
        logger.info(f"Fetching nearby stores slug={slug}")
        return self._fetch(url)

    def _enrich_products(
        self, store_id: int, products: List[Dict]
    ) -> List[Dict]:
        enriched: List[Dict] = []
        for product in products:
            pid = product.get("id")
            if pid is None:
                enriched.append(product)
                continue
            details = self.fetch_product_detail(store_id, pid)
            print(details)
            enriched.append(details)
        return enriched
