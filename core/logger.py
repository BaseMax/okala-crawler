import logging
import os
from config import LOG_DIR

os.makedirs(LOG_DIR, exist_ok=True)

_LOG_FILE = os.path.join(LOG_DIR, "crawler.log")
_FILE_FMT = logging.Formatter(
    "%(asctime)s | %(levelname)-8s | %(name)-20s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


class _AnsiFormatter(logging.Formatter):
    """Fallback colored formatter when rich is not installed."""

    _COLORS = {
        "DEBUG":    "\033[36m",   # cyan
        "INFO":     "\033[32m",   # green
        "WARNING":  "\033[33m",   # yellow
        "ERROR":    "\033[31m",   # red
        "CRITICAL": "\033[35m",   # magenta
    }
    _RESET = "\033[0m"
    _FMT   = "%(asctime)s | {color}%(levelname)-8s{reset} | %(name)-20s | %(message)s"

    def format(self, record: logging.LogRecord) -> str:
        color = self._COLORS.get(record.levelname, "")
        formatter = logging.Formatter(
            self._FMT.format(color=color, reset=self._RESET),
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        return formatter.format(record)


def get_logger(name: str = "okala") -> logging.Logger:
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger

    logger.setLevel(logging.DEBUG)
    logger.propagate = False

    fh = logging.FileHandler(_LOG_FILE, encoding="utf-8")
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(_FILE_FMT)
    logger.addHandler(fh)

    try:
        from rich.logging import RichHandler

        rh = RichHandler(
            level=logging.DEBUG,
            rich_tracebacks=True,
            show_path=False,
            markup=True,
            log_time_format="[%Y-%m-%d %H:%M:%S]",
        )
        logger.addHandler(rh)
    except ImportError:
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(_AnsiFormatter())
        logger.addHandler(ch)

    return logger
