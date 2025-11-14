# 2536. Increment Submatrices by One
# https://leetcode.com/problems/increment-submatrices-by-one/

from typing import List


# Based on Editorial's Approach: 2D Difference + Prefix Sum
class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        diff_array = [[0] * (n + 1) for _ in range(n + 1)]
        for r1, c1, r2, c2 in queries:
            diff_array[r1][c1] += 1
            diff_array[r2 + 1][c1] -= 1
            diff_array[r1][c2 + 1] -= 1
            diff_array[r2 + 1][c2 + 1] += 1

        ans = [[0] * n for _ in range(n)]
        for r in range(n):
            for c in range(n):
                col_diff = 0 if r == 0 else ans[r - 1][c]
                row_diff = 0 if c == 0 else ans[r][c - 1]
                diag_diff = 0 if r == 0 or c == 0 else ans[r - 1][c - 1]
                ans[r][c] = diff_array[r][c] + col_diff + row_diff - diag_diff
        return ans
