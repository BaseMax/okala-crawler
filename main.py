import sys

from core.crawler import OkalaCrawler
from core.logger import get_logger
from core.pipeline import DataPipeline

logger = get_logger("main")

# ── Store URLs ────────────────────────────────────────────────────────────────

STORES = [
    "https://www.okala.com/store/2319",
    "https://www.okala.com/store/10458",
    "https://www.okala.com/store/9871",
    "https://www.okala.com/store/9652",
    "https://www.okala.com/store/2318",
    "https://www.okala.com/store/10381",
    "https://www.okala.com/store/9020",
    "https://www.okala.com/store/9768",
    "https://www.okala.com/store/8840",
    "https://www.okala.com/store/5989",
    "https://www.okala.com/store/10650",
    "https://www.okala.com/store/7500",
    "https://www.okala.com/store/8131",
    "https://www.okala.com/store/9867",
    "https://www.okala.com/store/7791",
    "https://www.okala.com/store/8729",
    "https://www.okala.com/store/9991",
    "https://www.okala.com/store/8662",
]

# ── Categories (slug, rootId) ─────────────────────────────────────────────────

CATEGORIES = [
    ("kalabarg",           1467),
    ("refreshments",       1467),
    ("dairy-products",     1462),
    ("groceries",          1461),
    ("home-hygiene",       1471),
    ("beverages",          1465),
    ("spices",             1469),
    ("canned-ready-food",  1464),
    ("cosmetics-hygiene",  1472),
    ("proteins",           1463),
    ("breakfast-goods",    1466),
    ("home-stuff",         1473),
    ("baby-mother-care",   1474),
    ("fruits-vegetables",  1470),
    ("nuts-sweets",        1468),
    ("multiples",          1850),
]

# ── Request headers ───────────────────────────────────────────────────────────
# Replace the Bearer token with a fresh one before running.

HEADERS = {
    "Authorization": (
        "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjEzRjRFNUExQ0NGNUU4NjRBQTI3MzgyMkM3OENF"
        "RTIxQTM4MkRBOENSUzI1NiIsInR5cCI6ImF0K2p3dCIsIng1dCI6IkVfVGxvY3oxNkdTcUp6Z2l4"
        "NHplSWFPQzJvdyJ9.eyJuYmYiOjE3ODAwNTIxMjAsImV4cCI6MTc4MDA1MzkyMCwiaXNzIjoiaHR"
        "0cDovL2NlcmJlcnVzLm1lbWJlcnNoaXAiLCJjbGllbnRfaWQiOiJjdXN0b21lcl9jbGllbnRfaW"
        "QiLCJzdWIiOiIxMTE1NzA1MCIsImF1dGhfdGltZSI6MTc4MDA1MDIxNCwiaWRwIjoibG9jYWwiLCJ"
        "1c2VySWQiOiIxMTE1NzA1MCIsInVzZXJuYW1lIjoiMDkxMzQ5NTA3ODciLCJhbHRlcm5hdGl2ZUN"
        "1c3RvbWVySWQiOiIxMTE1NzA1MCIsInRlbmFudCI6Im9rYWxhIiwidG9rZW4taWQiOiJjMjc4OTcy"
        "Ni0wNjhlLTQ3MDYtYTgwYi00ZDNjMzBmNzkxMzVfOWFjYTg2ODItMjA3YS00MjkwLTgxMzAtZjYx"
        "NWNiZGM2NWJiIiwiY2VyYmVydXNJZCI6ImMyNzg5NzI2LTA2OGUtNDcwNi1hODBiLTRkM2MzMGY3"
        "OTEzNSIsImp0aSI6IkUxRDEwRkZGRkM0QUZGQTE2RkZCRDFBMDUxOEZCODJDIiwiaWF0IjoxNzgw"
        "MDUyMTIwLCJzY29wZSI6WyJvZmZsaW5lX2FjY2VzcyJdLCJhbXIiOlsiY3VzdG9tZXJfZ3JhbnRf"
        "dHlwZSJdfQ.HM1nH-plzP4JXg8UUcCAZdUs4Vo_Nmqaj7g6cDSO1dEDWk1f9rmddKaKsfVaO2qDc"
        "KccZJ58cZQJ71Km3XXadXOzZPn7ic9cNERiLazDO1SjBznxyI6ncdSg-rQ0judXwhElW47oQa1JAF"
        "vJiEGv_Bg1PaVFsCnzaqLtSpXFdyfGApUMVpymkpCr1um8aK2HDHYkiv8dgZxdTKlUnWNktXqFDEK"
        "in0jvhTs9uupJE6ITaIlOft8eKZiufznlaIQNTnTfKdwaDxo3x7M-JgnJ89ULUlwEcOBBgE0X-Q0q"
        "0vENK4whtLxxcPUefATvrQWsRHoz3jKLq7XXyyGVMGHDfw"
    ),
    "Accept":              "application/json, text/plain, */*",
    "User-Agent":          (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/148.0.0.0 Safari/537.36"
    ),
    "X-Skip-Authorization": "false",
    "ui-version":           "2.0",
    "source":               "okala",
}

# ── Helpers ───────────────────────────────────────────────────────────────────

def _store_id(url: str) -> int:
    return int(url.rstrip("/").split("/")[-1])


# ── Main ──────────────────────────────────────────────────────────────────────

def main() -> None:
    logger.info("=" * 60)
    logger.info("Okala Crawler — starting")
    logger.info(f"Stores: {len(STORES)}  |  Categories: {len(CATEGORIES)}")
    logger.info("=" * 60)

    crawler  = OkalaCrawler(headers=HEADERS)
    pipeline = DataPipeline()

    total    = len(STORES) * len(CATEGORIES)
    done     = 0
    failures = 0
    results  = []

    for store_url in STORES:
        sid = _store_id(store_url)
        store_index = STORES.index(store_url) + 1
        logger.info(f"── Store {sid} ({store_index}/{len(STORES)}) ──")

        for slug, cid in CATEGORIES:
            done += 1
            progress = f"[{done}/{total}]"
            try:
                result = crawler.crawl_store_category(
                    store_id=sid, slug=slug, category_id=cid
                )
                if result is not None:
                    results.append(result)
                    n = result["product_count"]
                    logger.info(f"{progress} store={sid} {slug} → {n} products")
                else:
                    failures += 1
                    logger.warning(f"{progress} store={sid} {slug} → no data")

            except Exception as exc:
                failures += 1
                logger.error(
                    f"{progress} store={sid} {slug} → unhandled error: {exc}",
                    exc_info=True,
                )

    pipeline.save_products(results)

    succeeded = done - failures
    cache_stats = crawler.cache.stats()
    logger.info("=" * 60)
    logger.info(f"Done: {succeeded}/{total} OK  |  {failures} failed")
    logger.info(
        f"Cache: {cache_stats['json_entries']} JSON entries "
        f"| {cache_stats['html_entries']} HTML entries"
    )
    logger.info("=" * 60)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.warning("Interrupted by user (Ctrl+C) — partial results may have been saved")
        sys.exit(0)
    except Exception as exc:
        logger.critical(f"Fatal error: {exc}", exc_info=True)
        sys.exit(1)
