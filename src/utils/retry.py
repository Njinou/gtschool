import logging
import time
from typing import Callable, Any

def retry(action: Callable[[], Any], retries: int = 3, delay: float = 1.0) -> Any:
    """Retries a given action a specified number of times with a delay."""
    for attempt in range(retries):
        try:
            return action()
        except Exception as e:
            logging.warning(f"Attempt {attempt + 1} failed: {e}")
            time.sleep(delay)
    raise Exception(f"Action failed after {retries} attempts")
