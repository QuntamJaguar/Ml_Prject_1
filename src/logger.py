import logging
import os
from datetime import datetime

# Set up logging
LOG_FILE = f"{datetime.utcnow().strftime('%Y-%m-%d_%H_%M_%S')}.log"  # Using UTC time
LOGS_DIR = "logs"
LOG_FILE_PATH = os.path.join(LOGS_DIR, LOG_FILE)

os.makedirs(LOGS_DIR, exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s - %(name)s - %(levelname)s] %(message)s",
    level=logging.INFO
)

# Example of usage
logger = logging.getLogger(__name__)  # Set the logger name to the current module name or any desired name

logger.info("This is an info message.")
logger.warning("This is a warning message.")
logger.error("This is an error message.")
logger.critical("This is a critical message.")
