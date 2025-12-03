import random
import time
from typing import Callable, TypeVar

T = TypeVar("T")


def retry_with_backoff(
    fn: Callable[[], T], max_retries: int = 3, base_delay: float = 1
) -> T:
    """Retry with exponential backoff + jitter."""
    for attempt in range(max_retries + 1):
        try:
            return fn()
        except Exception:
            if attempt == max_retries:
                raise
            delay = base_delay * (2**attempt)
            time.sleep(random.uniform(0, delay))
    raise RuntimeError("Unreachable")
