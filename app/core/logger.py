import logging
import sys
from pathlib import Path

log_dir = Path("logs")
log_dir.mkdir(exist_ok=True)

log_format = logging.Formatter(
    fmt="[%(asctime)s] - [%(levelname)s] - [%(filename)s] - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(log_format)

file_handler = logging.FileHandler("logs/app.log", encoding="utf-8")
file_handler.setFormatter(log_format)

logger = logging.getLogger("lms_backend")

logger.setLevel(logging.INFO)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

logger.propagate = False
