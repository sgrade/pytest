# 2464. Minimum Subarrays in a Valid Split
# https://leetcode.com/problems/minimum-subarrays-in-a-valid-split/

from typing import List
from math import gcd, inf

# Based on Editorial's Approach: Dynamic Programming
class Solution:
    def validSubarraySplit(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [inf] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                if gcd(nums[i - 1], nums[j - 1]) != 1:
                    dp[i] = min(dp[i], dp[j - 1] + 1)
        if dp[n] == inf:
            return -1
        return dp[n]
