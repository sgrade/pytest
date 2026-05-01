# 396. Rotate Function
# https://leetcode.com/problems/rotate-function/


# Based on Editorial's Approach: Dynamic Programming
class Solution:
    def maxRotateFunction(self, nums: list[int]) -> int:
        # F(k) = F(k-1) + sum(nums) - n * nums[n-k] after each rotation.
        n = len(nums)
        total = sum(nums)
        f = sum(i * x for i, x in enumerate(nums))
        best = f
        for k in range(1, n):
            f += total - n * nums[n - k]
            best = max(best, f)
        return best
