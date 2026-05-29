import time
from typing import Dict, Optional

import requests
import urllib3
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from config import BACKOFF_FACTOR, MAX_RETRIES, REQUEST_DELAY, TIMEOUT, VERIFY_SSL
from core.logger import get_logger

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

logger = get_logger("http-client")

class HTTPClient:
    def __init__(self) -> None:
        self.session = requests.Session()
        self._last_request_at: float = 0.0

        retry = Retry(
            total=MAX_RETRIES,
            backoff_factor=BACKOFF_FACTOR,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["GET", "POST"],
            raise_on_status=False,
        )
        adapter = HTTPAdapter(max_retries=retry)
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)

    def _throttle(self) -> None:
        elapsed = time.monotonic() - self._last_request_at
        if elapsed < REQUEST_DELAY:
            time.sleep(REQUEST_DELAY - elapsed)
        self._last_request_at = time.monotonic()

    def get(
        self,
        url: str,
        headers: Optional[Dict[str, str]] = None,
        params: Optional[Dict] = None,
    ) -> Optional[requests.Response]:
        self._throttle()
        try:
            logger.debug(f"GET {url}")
            response = self.session.get(
                url,
                headers=headers,
                params=params,
                timeout=TIMEOUT,
                verify=VERIFY_SSL,
            )
            return self._handle_response(response, url)

        except requests.exceptions.SSLError as exc:
            logger.error(f"SSL error - {url} | {exc}")
        except requests.exceptions.ConnectionError as exc:
            logger.error(f"Connection error - {url} | {exc}")
        except requests.exceptions.Timeout:
            logger.error(f"Timed out after {TIMEOUT}s - {url}")
        except requests.exceptions.TooManyRedirects:
            logger.error(f"Too many redirects - {url}")
        except requests.exceptions.RequestException as exc:
            logger.error(f"Request failed - {url} | {exc}")
        except Exception as exc:
            logger.critical(f"Unexpected error - {url} | {exc}", exc_info=True)

        return None

    @staticmethod
    def _handle_response(
        response: requests.Response, url: str
    ) -> Optional[requests.Response]:
        code = response.status_code

        if code == 200:
            logger.info(f"[200 OK] {url}")
            return response

        if code == 401:
            logger.error(
                f"[401 Unauthorized] {url} - Bearer token may be expired or invalid"
            )
            return None

        if code == 403:
            logger.error(f"[403 Forbidden] {url} - access denied")
            return None

        if code == 404:
            logger.warning(f"[404 Not Found] {url}")
            return None

        if code == 429:
            logger.warning(f"[429 Too Many Requests] {url} - cooling down 15 s")
            time.sleep(15)
            return None

        if 500 <= code < 600:
            logger.error(f"[{code} Server Error] {url}")
            return None

        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as exc:
            logger.error(f"[{code} HTTP Error] {url} | {exc}")
            return None

        return response
