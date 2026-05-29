import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from config import TIMEOUT, MAX_RETRIES, BACKOFF_FACTOR, VERIFY_SSL
from core.logger import get_logger

logger = get_logger("http-client")

class HTTPClient:
    def __init__(self):
        self.session = requests.Session()

        retry = Retry(
            total=MAX_RETRIES,
            backoff_factor=BACKOFF_FACTOR,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["GET", "POST"]
        )

        adapter = HTTPAdapter(max_retries=retry)
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)

    def get(self, url, headers=None):
        try:
            logger.info(f"GET {url}")

            response = self.session.get(
                url,
                headers=headers,
                timeout=TIMEOUT,
                verify=VERIFY_SSL,
            )

            response.raise_for_status()
            return response

        except requests.RequestException as e:
            logger.error(f"Request failed: {url} | {e}")
            return None