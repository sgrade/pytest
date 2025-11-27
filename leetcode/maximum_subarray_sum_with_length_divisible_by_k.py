# 3381. Maximum Subarray Sum With Length Divisible by K
# https://leetcode.com/problems/maximum-subarray-sum-with-length-divisible-by-k/

import sys


# Based on Editorial's Approach: Prefix Sum
class Solution:
    def maxSubarraySum(self, nums: list[int], k: int) -> int:
        n = len(nums)
        prefix_sum = 0
        max_sum = -sys.maxsize
        k_sum = [sys.maxsize // 2] * k
        k_sum[k - 1] = 0
        for i in range(n):
            prefix_sum += nums[i]
            max_sum = max(max_sum, prefix_sum - k_sum[i % k])
            k_sum[i % k] = min(k_sum[i % k], prefix_sum)
        return max_sum
