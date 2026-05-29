# core/logger.py
import logging
import os
from config import LOG_DIR

os.makedirs(LOG_DIR, exist_ok=True)

def get_logger(name="okala-crawler"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:
        fmt = logging.Formatter(
            "[%(asctime)s] [%(levelname)s] %(name)s: %(message)s"
        )

        file_handler = logging.FileHandler(
            os.path.join(LOG_DIR, "crawler.log"),
            encoding="utf-8"
        )
        file_handler.setFormatter(fmt)

        console = logging.StreamHandler()
        console.setFormatter(fmt)

        logger.addHandler(file_handler)
        logger.addHandler(console)

    return logger