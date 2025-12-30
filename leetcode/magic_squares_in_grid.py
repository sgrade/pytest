# 840. Magic Squares In Grid
# https://leetcode.com/problems/magic-squares-in-grid/


class Solution:
    def numMagicSquaresInside(self, grid: list[list[int]]) -> int:
        def is_magic_square(top_r: int, left_c: int) -> int:
            # Reference sum
            sum_diag = (
                grid[top_r][left_c]
                + grid[top_r + 1][left_c + 1]
                + grid[top_r + 2][left_c + 2]
            )
            sum_anti_diag = (
                grid[top_r + 2][left_c]
                + grid[top_r + 1][left_c + 1]
                + grid[top_r][left_c + 2]
            )
            if sum_diag != sum_anti_diag:
                return 0

            seen = set[int]()  # To store unique numbers
            # Checking rows
            for r in range(top_r, top_r + 3):
                sum_r = 0
                for c in range(left_c, left_c + 3):
                    # Check if the numbers are in the allowed range
                    if not (1 <= grid[r][c] <= 9):
                        return 0
                    seen.add(grid[r][c])
                    sum_r += grid[r][c]
                if sum_r != sum_diag:
                    return 0
            # Check if the numbers are unique
            if len(seen) < 9:
                return 0

            # Checking columns
            for c in range(left_c, left_c + 3):
                sum_c = 0
                for r in range(top_r, top_r + 3):
                    sum_c += grid[r][c]
                if sum_c != sum_diag:
                    return 0

            return 1

        magic_squares = 0
        for top_r in range(0, len(grid) - 2):
            for left_c in range(0, len(grid[0]) - 2):
                magic_squares += is_magic_square(top_r, left_c)
        return magic_squares
