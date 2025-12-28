# 1351. Count Negative Numbers in a Sorted Matrix
# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/


class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        negatives = 0
        rows, cols, max_col = len(grid), len(grid[0]), len(grid[0])
        for row in grid:
            for col in range(max_col):
                if row[col] < 0:
                    negatives += cols - col
                    max_col = col + 1
                    break
        return negatives
