# 2654. Minimum Number of Operations to Make All Array Elements Equal to 1
# https://leetcode.com/problems/minimum-number-of-operations-to-make-all-array-elements-equal-to-1/

from math import gcd
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ones, g = 0, 0
        for num in nums:
            if num == 1:
                ones += 1
            g = gcd(g, num)

        if ones > 0:
            return n - ones
        if g > 1:
            return -1

        min_len = n
        for lo in range(n):
            g = 0
            for hi in range(lo, n):
                g = gcd(g, nums[hi])
                if g == 1:
                    min_len = min(min_len, hi - lo + 1)
                    break

        min_ops_to_get_one = min_len - 1
        ops = min_ops_to_get_one + (n - 1)
        return ops
