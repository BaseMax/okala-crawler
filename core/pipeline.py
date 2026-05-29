import json
import os
from config import OUTPUT_DIR

os.makedirs(OUTPUT_DIR, exist_ok=True)

class DataPipeline:
    def save_store_data(self, data):
        path = os.path.join(OUTPUT_DIR, "stores.json")
        self._write(path, data)

    def save_products(self, data):
        path = os.path.join(OUTPUT_DIR, "products.json")
        self._write(path, data)

    def _write(self, path, data):
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)