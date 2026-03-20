# 3567. Minimum Absolute Difference in Sliding Submatrix
# https://leetcode.com/problems/minimum-absolute-difference-in-sliding-submatrix/

import math


# Based on Editorial's Approach: Sorting
# For each k×k submatrix, sort its elements and find the minimum
# difference between consecutive distinct values.
class Solution:
    def minAbsDiff(self, grid: list[list[int]], k: int) -> list[list[int]]:
        rows, cols = len(grid), len(grid[0])
        ans = [[0] * (cols - k + 1) for _ in range(rows - k + 1)]

        for r in range(rows - k + 1):
            for c in range(cols - k + 1):
                # Collect and sort all elements in the k×k submatrix.
                sub = sorted(
                    grid[i][j] for i in range(r, r + k) for j in range(c, c + k)
                )
                # Min difference between consecutive distinct values.
                min_diff = math.inf
                for i in range(1, len(sub)):
                    if sub[i] != sub[i - 1]:
                        min_diff = min(min_diff, sub[i] - sub[i - 1])
                if min_diff != math.inf:
                    ans[r][c] = int(min_diff)

        return ans
