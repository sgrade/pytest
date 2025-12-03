# Problem 1: Implement the `tail` Command

**Source:** Google SRE Interview (Glassdoor)

## Problem Statement

Implement a function that returns the last `n` lines of a file, similar to the Unix `tail` command.

**Constraints:**
- The file may be very large (cannot fit in memory)
- Must be memory-efficient
- Handle edge cases: file has fewer than n lines, empty file

## Function Signature

```python
def tail(filename: str, n: int) -> list[str]:
    """Return the last n lines of a file."""
    pass
```

## Your Solution

Create your solution in `solutions/01_tail.py`

