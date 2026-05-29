# Okala Crawler

A Python crawler for extracting product data from [okala.com](https://www.okala.com) (an Iranian online grocery and supermarket platform). It crawls multiple stores across all product categories, caches responses locally, and writes structured JSON output.

## Features

- Crawls **18 stores** across **16 product categories**
- Optional full product detail (PDP) fetching per product
- Nearby-stores query support by GPS coordinates
- Disk-based JSON cache with configurable TTL (default 24 h) and atomic writes
- Automatic HTTP retry with exponential back-off on `429`/`5xx` responses
- Request throttling to avoid rate limiting
- Colorized console logging via `rich` with parallel file logging

## Project Structure

```
okala-crawler/
├── main.py           # Entry point - store/category iteration
├── config.py         # All tuneable settings
├── requirements.txt
├── core/
│   ├── crawler.py    # OkalaCrawler - fetches and enriches products
│   ├── pipeline.py   # DataPipeline - saves outputs atomically
│   ├── cache.py      # CacheManager - JSON/HTML cache with TTL
│   ├── client.py     # HTTPClient - retries, throttle, error handling
│   └── logger.py     # Structured logging (rich + file)
├── cache/
│   ├── json/         # Cached API responses
│   └── html/         # Cached HTML (reserved)
├── logs/
│   └── crawler.log
└── outputs/
    └── products.json
```

## Requirements

- Python 3.9+
- Dependencies listed in `requirements.txt`:

```
requests>=2.31.0
urllib3>=2.0.0
rich>=13.0.0
```

## Installation

```bash
git clone https://github.com/BaseMax/okala-crawler.git
cd okala-crawler
pip install -r requirements.txt
```

## Configuration

All settings live in `config.py`:

| Setting | Default | Description |
|---|---|---|
| `TIMEOUT` | `60` | HTTP request timeout (seconds) |
| `MAX_RETRIES` | `5` | Retry attempts on `429`/`5xx` |
| `BACKOFF_FACTOR` | `2.0` | Exponential back-off multiplier |
| `REQUEST_DELAY` | `0.5` | Minimum delay between requests (seconds) |
| `CACHE_TTL` | `86400` | Cache lifetime in seconds (`0` = never expire) |
| `FETCH_PRODUCT_DETAILS` | `False` | Fetch full PDP for every product (multiplies requests) |
| `LAT` / `LON` | Tehran – Darakeh | Coordinates used for nearby-store queries |

### Bearer Token

The API requires a valid JWT. Update the `Authorization` header in `main.py`:

```python
HEADERS = {
    "Authorization": "Bearer <your-token>",
    ...
}
```

Tokens expire; replace when you receive `401 Unauthorized` in the logs.

## Usage

```bash
python main.py
```

Progress is printed to the console and written to `logs/crawler.log`. Results are saved atomically to `outputs/products.json`.

### Output Format

```json
{
  "meta": {
    "generated_at": "2026-05-29T12:00:00",
    "store_count": 18,
    "category_entries": 288,
    "total_product_count": 4200
  },
  "data": [
    {
      "store_id": 2319,
      "category_slug": "dairy-products",
      "category_id": 1462,
      "product_count": 35,
      "products": [ ... ]
    }
  ]
}
```

## Supported Categories

| Slug | Category ID |
|---|---|
| `kalabarg` | 1467 |
| `refreshments` | 1467 |
| `dairy-products` | 1462 |
| `groceries` | 1461 |
| `home-hygiene` | 1471 |
| `beverages` | 1465 |
| `spices` | 1469 |
| `canned-ready-food` | 1464 |
| `cosmetics-hygiene` | 1472 |
| `proteins` | 1463 |
| `breakfast-goods` | 1466 |
| `home-stuff` | 1473 |
| `baby-mother-care` | 1474 |
| `fruits-vegetables` | 1470 |
| `nuts-sweets` | 1468 |
| `multiples` | 1850 |

## Cache

Responses are cached under `cache/json/` as MD5-keyed files with accompanying `.meta.json` files storing TTL metadata. Stale entries are evicted automatically on the next read. Set `CACHE_TTL = 0` in `config.py` to cache indefinitely.

## License

MIT License

Copyright (c) 2026 Seyyed Ali Mohammadiyeh (Max Base)
