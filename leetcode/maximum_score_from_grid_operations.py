# 3225. Maximum Score From Grid Operations
# https://leetcode.com/problems/maximum-score-from-grid-operations/


# Based on Editorial's Approach: Dynamic Programming
class Solution:
    def maximumScore(self, grid: list[list[int]]) -> int:
        n = len(grid[0])
        if n == 1:
            return 0

        # Prefix sums per column for O(1) vertical ranges.
        col_sum = [[0] * (n + 1) for _ in range(n)]
        for c in range(n):
            for r in range(1, n + 1):
                col_sum[c][r] = col_sum[c][r - 1] + grid[r - 1][c]

        # dp[i][curr_h][prev_h]: max score for columns 0..i with those heights.
        dp = [[[0] * (n + 1) for _ in range(n + 1)] for _ in range(n)]
        prev_max = [[0] * (n + 1) for _ in range(n + 1)]
        prev_suffix_max = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(1, n):
            for curr_h in range(n + 1):
                for prev_h in range(n + 1):
                    if curr_h <= prev_h:
                        extra = col_sum[i][prev_h] - col_sum[i][curr_h]
                        best = prev_suffix_max[prev_h][0] + extra
                    else:
                        extra = col_sum[i - 1][curr_h] - col_sum[i - 1][prev_h]
                        best = max(
                            prev_suffix_max[prev_h][curr_h],
                            prev_max[prev_h][curr_h] + extra,
                        )
                    dp[i][curr_h][prev_h] = max(dp[i][curr_h][prev_h], best)

            for curr_h in range(n + 1):
                prev_max[curr_h][0] = dp[i][curr_h][0]
                for prev_h in range(1, n + 1):
                    penalty = (
                        col_sum[i][prev_h] - col_sum[i][curr_h]
                        if prev_h > curr_h
                        else 0
                    )
                    prev_max[curr_h][prev_h] = max(
                        prev_max[curr_h][prev_h - 1],
                        dp[i][curr_h][prev_h] - penalty,
                    )

                prev_suffix_max[curr_h][n] = dp[i][curr_h][n]
                for prev_h in range(n - 1, -1, -1):
                    prev_suffix_max[curr_h][prev_h] = max(
                        prev_suffix_max[curr_h][prev_h + 1],
                        dp[i][curr_h][prev_h],
                    )

        return max(max(dp[n - 1][n]), max(dp[n - 1][0]))
