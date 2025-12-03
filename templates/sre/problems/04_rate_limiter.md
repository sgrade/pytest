# Problem 4: Implement a Rate Limiter

**Source:** Google, Uber, Stripe SRE/Backend Interviews

## Problem Statement

Implement a sliding window rate limiter that allows at most `limit` requests per `window_seconds`.

## Function Signature

```python
class RateLimiter:
    def __init__(self, limit: int, window_seconds: float):
        """
        Initialize rate limiter.
        limit: max requests allowed in window
        window_seconds: sliding window size
        """
        pass
    
    def allow(self) -> bool:
        """
        Check if request is allowed.
        Returns True and records request if under limit.
        Returns False if rate limit exceeded.
        """
        pass
```

## Follow-up Questions (commonly asked)

1. How would you implement this in a distributed system?
2. What's the difference between sliding window and fixed window?
3. How would you handle burst traffic?

## Your Solution

Create your solution in `solutions/04_rate_limiter.py`

