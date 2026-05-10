# 2770. Maximum Number of Jumps to Reach the Last Index
# https://leetcode.com/problems/maximum-number-of-jumps-to-reach-the-last-index/


# Based on Editorial's Approach 2: Dynamic Programming
class Solution:
    def maximumJumps(self, nums: list[int], target: int) -> int:
        n = len(nums)
        # dp[i] = max jumps to reach index i, or -inf if unreachable.
        dp = [float("-inf")] * n
        dp[0] = 0

        for i in range(1, n):
            for j in range(i):
                if abs(nums[i] - nums[j]) <= target:
                    dp[i] = max(dp[i], dp[j] + 1)

        return -1 if dp[-1] < 0 else int(dp[-1])
