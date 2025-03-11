"""Logger module for tracking operations performed by the calculator."""

import logging
from pathlib import Path

LOG_FILE = Path("operations.log")

# Configure logging to write to a file
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format="%(message)s")

class Logger:
    """Logger class to log operations performed by the calculator."""

    @staticmethod
    def log(message: str) -> None:
        """Log a message to the operations log file and force flush."""
        logging.info(message)

        # Flush logging handlers to ensure the message is written immediately
        for handler in logging.getLogger().handlers:
            handler.flush()
