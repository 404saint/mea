import time
from config import SCAN_DELAY
from utils.logger import setup_logger

logger = setup_logger()

class RateLimiter:
    """ 
    Controls request rate to avoid aggressive behavior
    against industrial devices.
    """

    def __init__(self, delay=SCAN_DELAY):
        self.delay = delay
        self.last_request_time = 0

    def wait(self):
        """
        Ensures minimum delay between requests.
        """
        now = time.time()
        elapsed = now - self.last_request_time

        if elapsed < self.delay:
            sleep_time = self.delay - elapsed
            logger.debug(f"Rate limiting: sleeping {sleep_time:.3f}s")
            time.sleep(sleep_time)

        self.last_request_time = time.time()