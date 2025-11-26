# 2435. Paths in Matrix Whose Sum Is Divisible by K
# https://leetcode.com/problems/paths-in-matrix-whose-sum-is-divisible-by-k/


# Based on Editorial's Approach: Dynamic Programming
class Solution:
    def numberOfPaths(self, grid: list[list[int]], k: int) -> int:
        MOD = 10**9 + 7
        rows, cols = len(grid), len(grid[0])

        dp = [[[0] * k for _ in range(cols + 1)] for _ in range(rows + 1)]
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                if i == 1 and j == 1:
                    dp[i][j][grid[0][0] % k] = 1
                    continue

                val = grid[i - 1][j - 1] % k
                for r in range(k):
                    prev_mod = (r - val + k) % k
                    dp[i][j][r] = (
                        dp[i - 1][j][prev_mod] + dp[i][j - 1][prev_mod]
                    ) % MOD
        return dp[rows][cols][0]
