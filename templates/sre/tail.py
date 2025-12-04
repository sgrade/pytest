"""Problem 1: Implement the `tail` command."""

from collections import deque


def tail(filename: str, n: int) -> list[str]:
    """Return the last n lines of a file. O(file_size) time, O(n) space."""
    if n <= 0:
        return []
    with open(filename) as f:
        return list(deque(f, maxlen=n))


def tail_backward(filename: str, n: int, chunk_size: int = 1024) -> list[str]:
    """Return the last n lines by reading backward. O(n * line_len) time."""
    if n <= 0:
        return []

    with open(filename, "rb") as f:
        f.seek(0, 2)  # seek to end
        size = f.tell()
        if size == 0:
            return []

        lines: list[str] = []
        remaining = size

        while len(lines) <= n and remaining > 0:
            read_size = min(chunk_size, remaining)
            remaining -= read_size
            f.seek(remaining)
            chunk = f.read(read_size).decode()
            lines = chunk.splitlines() + lines

        return lines[-n:]
