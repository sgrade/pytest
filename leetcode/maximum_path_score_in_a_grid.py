# 3742. Maximum Path Score in a Grid
# https://leetcode.com/problems/maximum-path-score-in-a-grid/

# Based on Editorial's Approach: Dynamic Programming
class Solution:
    def maxPathScore(self, grid, k):
        rows, cols = len(grid), len(grid[0])

        neg_inf = float("-inf")
        dp = [[[neg_inf] * (k + 1) for _ in range(cols)] for _ in range(rows)]
        dp[0][0][0] = 0

        # dp[i][j][c] = best sum reaching (i,j) using c removals on the path.
        for i in range(rows):
            for j in range(cols):
                for c in range(k + 1):
                    if dp[i][j][c] == neg_inf:
                        continue
                    for di, dj in ((1, 0), (0, 1)):
                        ni, nj = i + di, j + dj
                        if ni >= rows or nj >= cols:
                            continue
                        val = grid[ni][nj]
                        cost = 0 if val == 0 else 1
                        if c + cost <= k:
                            dp[ni][nj][c + cost] = max(
                                dp[ni][nj][c + cost],
                                dp[i][j][c] + val,
                            )

        ans = max(dp[rows - 1][cols - 1])
        return -1 if ans < 0 else ans
