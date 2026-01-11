# 85. Maximal Rectangle
# https://leetcode.com/problems/maximal-rectangle/

# Based on Editorial's Approach 2: Dynamic Programming - Better Brute Force on Histograms
class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        ans = 0
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0] * cols for _ in range(rows)]
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == "1":
                    dp[row][col] = 1 if col == 0 else dp[row][col - 1] + 1
                    width = dp[row][col]
                    for r in range(row, -1, -1):
                        width = min(width, dp[r][col])
                        ans = max(ans, width * (row - r + 1))
        return ans
