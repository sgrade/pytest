# 2916. Subarrays Distinct Element Sum of Squares II
# https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-ii/


class RangeFenwickTree:
    """Fenwick tree (1-indexed) with range add and range sum."""

    def __init__(self, size: int):
        self._size = size
        # value[i] contributes as: prefix_sum(k) = k * sum(_coef) - sum(_bias)
        self._coef = [0] * (size + 1)
        self._bias = [0] * (size + 1)

    def range_add(self, left: int, right: int, delta: int) -> None:
        self._point_add(left, delta)
        self._point_add(right + 1, -delta)

    def range_sum(self, left: int, right: int) -> int:
        return self._prefix_sum(right) - self._prefix_sum(left - 1)

    def _point_add(self, pos: int, delta: int) -> None:
        bias_delta = (pos - 1) * delta
        while pos <= self._size:
            self._coef[pos] += delta
            self._bias[pos] += bias_delta
            pos += pos & -pos

    def _prefix_sum(self, pos: int) -> int:
        coef_sum = bias_sum = 0
        i = pos
        while i > 0:
            coef_sum += self._coef[i]
            bias_sum += self._bias[i]
            i -= i & -i
        return pos * coef_sum - bias_sum


# Based on Editorial's Approach: Binary Indexed Tree
class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        mod = 10**9 + 7
        n = len(nums)
        # tree[left] = number of distinct values in nums[left..right]
        tree = RangeFenwickTree(n)
        last_pos = {}  # value -> last 1-indexed position seen
        squares_sum = 0  # sum of squared counts of subarrays ending at right
        total = 0
        for right, num in enumerate(nums, start=1):
            first = last_pos.get(num, 0) + 1
            # Starts in [first, right] gain one distinct value:
            # (c + 1)^2 - c^2 = 2c + 1, summed over the range.
            gain = 2 * tree.range_sum(first, right) + (right - first + 1)
            squares_sum = (squares_sum + gain) % mod
            total = (total + squares_sum) % mod
            tree.range_add(first, right, 1)
            last_pos[num] = right
        return total
