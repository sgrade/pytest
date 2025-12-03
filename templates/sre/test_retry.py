"""Tests for retry template."""

import pytest
from retry import retry_with_backoff


def test_successful_call():
    assert retry_with_backoff(lambda: 42) == 42


def test_retry_then_succeed():
    attempts = [0]

    def flaky():
        attempts[0] += 1
        if attempts[0] < 3:
            raise ValueError("fail")
        return "ok"

    result = retry_with_backoff(flaky, max_retries=3, base_delay=0.01)
    assert result == "ok"
    assert attempts[0] == 3


def test_exhausted_retries():
    with pytest.raises(ZeroDivisionError):
        retry_with_backoff(lambda: 1 / 0, max_retries=2, base_delay=0.01)
