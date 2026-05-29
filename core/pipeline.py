import json
import os
import tempfile
import time
from typing import Any, Dict, List, Optional

from config import OUTPUT_DIR
from core.logger import get_logger

logger = get_logger("pipeline")

os.makedirs(OUTPUT_DIR, exist_ok=True)


class DataPipeline:
    @staticmethod
    def _atomic_write(path: str, data: Any) -> None:
        dir_ = os.path.dirname(path)
        tmp_path: Optional[str] = None
        try:
            with tempfile.NamedTemporaryFile(
                "w", dir=dir_, encoding="utf-8", delete=False, suffix=".tmp"
            ) as tmp:
                json.dump(data, tmp, ensure_ascii=False, indent=2)
                tmp_path = tmp.name
            os.replace(tmp_path, path)
            logger.info(f"Saved → {path}")
        except OSError as exc:
            logger.error(f"Failed to save {path}: {exc}")
            if tmp_path and os.path.exists(tmp_path):
                os.remove(tmp_path)
            raise

    def save_products(self, results: List[Dict]) -> None:
        valid = [r for r in results if r is not None]
        total_products = sum(r.get("product_count", 0) for r in valid)
        unique_stores = len({r["store_id"] for r in valid})

        payload = {
            "meta": {
                "generated_at":         time.strftime("%Y-%m-%dT%H:%M:%S"),
                "store_count":          unique_stores,
                "category_entries":     len(valid),
                "total_product_count":  total_products,
            },
            "data": valid,
        }

        path = os.path.join(OUTPUT_DIR, "products.json")
        self._atomic_write(path, payload)
        logger.info(
            f"Output: {unique_stores} stores | "
            f"{len(valid)} category entries | "
            f"{total_products} products"
        )

    def save_stores(self, stores: List[Dict]) -> None:
        path = os.path.join(OUTPUT_DIR, "stores.json")
        self._atomic_write(path, {
            "meta": {
                "generated_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
                "count":        len(stores),
            },
            "data": stores,
        })
