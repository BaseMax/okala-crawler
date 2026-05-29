from core.crawler import OkalaCrawler
from core.pipeline import DataPipeline

stores = [
    "https://www.okala.com/store/2319",
    "https://www.okala.com/store/10458",
]

categories = [
    ("refreshments", 1467),
    ("groceries", 1461),
]

HEADERS = {
    "Authorization": "Bearer YOUR_TOKEN",
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json",
}

def extract_store_id(url):
    return int(url.split("/")[-1])

def main():
    crawler = OkalaCrawler()
    pipeline = DataPipeline()

    all_results = []

    for store_url in stores:
        store_id = extract_store_id(store_url)

        for slug, cid in categories:
            result = crawler.crawl_store_category(
                store_id=store_id,
                category_slug=slug,
                category_id=cid,
                headers=HEADERS
            )

            if result:
                all_results.append(result)

    pipeline.save_products(all_results)

if __name__ == "__main__":
    main()