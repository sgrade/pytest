# 3643. Flip Square Submatrix Vertically
# https://leetcode.com/problems/flip-square-submatrix-vertically/


class Solution:
    def reverseSubmatrix(
        self, grid: list[list[int]], x: int, y: int, k: int
    ) -> list[list[int]]:
        bot_row = x + k - 1
        for top_row in range(x, x + k):
            if top_row >= bot_row:
                break
            for col in range(y, y + k):
                grid[top_row][col], grid[bot_row][col] = (
                    grid[bot_row][col],
                    grid[top_row][col],
                )
            bot_row -= 1
        return grid
