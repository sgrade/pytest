# 3505. Minimum Operations to Make Elements Within K Subarrays Equal
# https://leetcode.com/problems/minimum-operations-to-make-elements-within-k-subarrays-equal/


from collections import defaultdict
from heapq import heappop, heappush
from math import inf


class SlidingMedian:
    """Window multiset that reports the cost of making all values equal.

    `low` is a max-heap (negated values) with the smaller half, `high` is a
    min-heap with the larger half; len(low) == len(high) or one more, so
    the median is -low[0]. Removals are lazy: values are marked in
    `pending_removal` and popped only once they reach a heap top.
    """

    def __init__(self) -> None:
        self.low: list[int] = []
        self.high: list[int] = []
        self.pending_removal: defaultdict[int, int] = defaultdict(int)
        self.low_size = self.high_size = 0  # Counts of live elements.
        self.low_sum = self.high_sum = 0

    def _prune(self, heap: list[int], sign: int) -> None:
        # Drop lazily removed values sitting at the top of the heap.
        while heap and self.pending_removal[sign * heap[0]]:
            self.pending_removal[sign * heap[0]] -= 1
            heappop(heap)

    def _move_low_to_high(self) -> None:
        num = -heappop(self.low)
        heappush(self.high, num)
        self.low_size -= 1
        self.low_sum -= num
        self.high_size += 1
        self.high_sum += num
        self._prune(self.low, -1)

    def _move_high_to_low(self) -> None:
        num = heappop(self.high)
        heappush(self.low, -num)
        self.high_size -= 1
        self.high_sum -= num
        self.low_size += 1
        self.low_sum += num
        self._prune(self.high, 1)

    def _rebalance(self) -> None:
        if self.low_size > self.high_size + 1:
            self._move_low_to_high()
        elif self.high_size > self.low_size:
            self._move_high_to_low()

    def add(self, num: int) -> None:
        if not self.low or num <= -self.low[0]:
            heappush(self.low, -num)
            self.low_size += 1
            self.low_sum += num
        else:
            heappush(self.high, num)
            self.high_size += 1
            self.high_sum += num
        self._rebalance()

    def remove(self, num: int) -> None:
        self.pending_removal[num] += 1
        if num <= -self.low[0]:
            self.low_size -= 1
            self.low_sum -= num
            self._prune(self.low, -1)
        else:
            self.high_size -= 1
            self.high_sum -= num
            self._prune(self.high, 1)
        self._rebalance()

    def cost(self) -> int:
        # Sum of |v - median| = (median * |low| - low_sum)
        #                     + (high_sum - median * |high|).
        median = -self.low[0]
        return (
            median * (self.low_size - self.high_size)
            - self.low_sum
            + self.high_sum
        )


# Based on Editorial's Approach 1: Sliding Window + Two Heaps + Mathematics +
# Dynamic Programming
class Solution:
    def minOperations(self, nums: list[int], x: int, k: int) -> int:
        n = len(nums)

        # window_cost[i]: min ops to make nums[i - x + 1 .. i] all equal,
        # i.e. shift every element to the window's median.
        window_cost = [0] * n
        window = SlidingMedian()
        for i, num in enumerate(nums):
            window.add(num)
            if i >= x:
                window.remove(nums[i - x])
            if i >= x - 1:
                window_cost[i] = window.cost()

        # dp[j][i]: min ops to pick j non-overlapping windows from the first
        # i elements. Either skip element i - 1, or end a window at it.
        dp = [[0.0] * (n + 1)] + [[inf] * (n + 1) for _ in range(k)]
        for j in range(1, k + 1):
            for i in range(j * x, n + 1):
                dp[j][i] = min(
                    dp[j][i - 1], dp[j - 1][i - x] + window_cost[i - 1]
                )
        return int(dp[k][n])
