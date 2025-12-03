import time
from collections import deque


class RateLimiter:
    """Sliding window rate limiter."""

    def __init__(self, limit: int, window_seconds: float) -> None:
        self.limit = limit
        self.window = window_seconds
        self.requests: deque[float] = deque()

    def allow(self) -> bool:
        now = time.time()
        # Remove expired requests
        while self.requests and self.requests[0] < now - self.window:
            self.requests.popleft()

        if len(self.requests) < self.limit:
            self.requests.append(now)
            return True
        return False
