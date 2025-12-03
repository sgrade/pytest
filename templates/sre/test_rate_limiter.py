"""Tests for rate_limiter template."""

import time

from rate_limiter import RateLimiter


def test_allows_within_limit():
    rl = RateLimiter(limit=3, window_seconds=0.1)
    assert rl.allow() is True
    assert rl.allow() is True
    assert rl.allow() is True


def test_blocks_over_limit():
    rl = RateLimiter(limit=3, window_seconds=0.1)
    rl.allow()
    rl.allow()
    rl.allow()
    assert rl.allow() is False


def test_allows_after_window():
    rl = RateLimiter(limit=2, window_seconds=0.05)
    rl.allow()
    rl.allow()
    assert rl.allow() is False
    time.sleep(0.06)
    assert rl.allow() is True
