# 3546. Equal Sum Grid Partition I
# https://leetcode.com/problems/equal-sum-grid-partition-i/


class Solution:
    def canPartitionGrid(self, grid: list[list[int]]) -> bool:
        total = sum(val for row in grid for val in row)
        if total % 2 != 0:
            return False
        half = total // 2

        # Try horizontal cuts between rows.
        running = 0
        for i in range(len(grid) - 1):
            running += sum(grid[i])
            if running == half:
                return True

        # Try vertical cuts between columns.
        running = 0
        for j in range(len(grid[0]) - 1):
            running += sum(grid[i][j] for i in range(len(grid)))
            if running == half:
                return True

        return False
