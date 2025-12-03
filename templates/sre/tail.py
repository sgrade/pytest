"""Problem 1: Implement the `tail` command."""

from collections import deque


def tail(filename: str, n: int) -> list[str]:
    """Return the last n lines of a file."""
    if n <= 0:
        return []
    with open(filename) as f:
        return list(deque(f, maxlen=n))
