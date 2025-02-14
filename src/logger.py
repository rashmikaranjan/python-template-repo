"""Logger module for tracking operations performed by the calculator."""

import logging
from pathlib import Path

# Configure logging to write to a file
LOG_FILE = Path("operations.log")
logging.basicConfig(filename=LOG_FILE, level=logging.INFO)

class Logger:
    """Logger class to log operations performed by the calculator."""

    @staticmethod
    def log(message: str) -> None:
        """Log a message to the operations log file."""
        logging.info(message)
