import logging
import os
from config import LOG_LEVEL, OUTPUT_DIR

def setup_logger(name="MEA"):
    """ 
    Creates and returns a configured logger instance.
    Logs to console and to a file inside OUTPUT_DIR.
    """
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Clear root logger handlers (important)
    root_logger = logging.getLogger()
    if root_logger.handlers:
        root_logger.handlers.clear()

    logger = logging.getLogger(name)
    logger.propagate = False  # prevent double logging

    # Prevent duplicate handlers
    if logger.handlers:
        return logger

    level = getattr(logging, LOG_LEVEL.upper(), logging.INFO)
    logger.setLevel(level)

    formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] %(message)s",
        "%Y-%m-%d %H:%M:%S"
    )

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # File handler
    file_handler = logging.FileHandler(os.path.join(OUTPUT_DIR, "mea.log"))
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger