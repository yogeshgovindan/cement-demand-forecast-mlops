import logging
import os
from datetime import datetime

from src.constants.paths import LOG_DIR


# Create log directory if not present
LOG_DIR.mkdir(
    exist_ok=True
)


# Create unique log file
LOG_FILE = (
    LOG_DIR /
    f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
)


logging.basicConfig(
    filename=LOG_FILE,
    format="[%(asctime)s] %(levelname)s %(name)s - %(message)s",
    level=logging.INFO,
)


logger = logging.getLogger("MLOPS")