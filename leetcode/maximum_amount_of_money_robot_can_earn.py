# 3418. Maximum Amount of Money Robot Can Earn
# https://leetcode.com/problems/maximum-amount-of-money-robot-can-earn/


# Based on Editorial's Approach 2: Dynamic Programming
class Solution:
    def maximumAmount(self, coins: list[list[int]]) -> int:
        # dp[j][k] = max coins reachable at column j with k neutralizations left
        num_cols = len(coins[0])
        dp = [[-(10**9)] * 3 for _ in range(num_cols + 1)]
        dp[1] = [0] * 3  # entry point: column 0, 0 coins, any neutralizations

        for row in coins:
            for j, x in enumerate(row):
                # Process k=2 before k=1 to use pre-update values (same row)
                for k in range(2, 0, -1):
                    best = max(dp[j][k], dp[j + 1][k])
                    skip = max(dp[j][k - 1], dp[j + 1][k - 1])
                    dp[j + 1][k] = max(best + x, skip)
                dp[j + 1][0] = max(dp[j][0], dp[j + 1][0]) + x

        return dp[num_cols][2]
