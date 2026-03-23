# 1594. Maximum Non Negative Product in a Matrix
# https://leetcode.com/problems/maximum-non-negative-product-in-a-matrix/


# Based on Editorial's Approach: Dynamic Programming
# Track both max and min products at each cell, since a negative value
# can flip the min into the new max (and vice versa).
class Solution:
    def maxProductPath(self, grid: list[list[int]]) -> int:
        mod = 10**9 + 7
        rows, cols = len(grid), len(grid[0])
        max_dp = [[0] * cols for _ in range(rows)]
        min_dp = [[0] * cols for _ in range(rows)]

        # Base cases: first cell, first column, first row.
        max_dp[0][0] = min_dp[0][0] = grid[0][0]
        for r in range(1, rows):
            max_dp[r][0] = min_dp[r][0] = max_dp[r - 1][0] * grid[r][0]
        for c in range(1, cols):
            max_dp[0][c] = min_dp[0][c] = max_dp[0][c - 1] * grid[0][c]

        for r in range(1, rows):
            for c in range(1, cols):
                candidates = (
                    max_dp[r][c - 1] * grid[r][c],
                    max_dp[r - 1][c] * grid[r][c],
                    min_dp[r][c - 1] * grid[r][c],
                    min_dp[r - 1][c] * grid[r][c],
                )
                max_dp[r][c] = max(candidates)
                min_dp[r][c] = min(candidates)

        ans = max_dp[rows - 1][cols - 1]
        return -1 if ans < 0 else ans % mod
