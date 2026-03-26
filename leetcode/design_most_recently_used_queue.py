# 1756. Design Most Recently Used Queue
# https://leetcode.com/problems/design-most-recently-used-queue/


# Based on Editorial's Approach 1: Brute Force with Array Queue
class MRUQueue:
    def __init__(self, n: int):
        self.queue = list(range(1, n + 1))

    def fetch(self, k: int) -> int:
        # Remove k-th element (1-indexed) and move it to the back.
        value = self.queue.pop(k - 1)
        self.queue.append(value)
        return value
