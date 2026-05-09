# 1914. Cyclically Rotating a Grid
# https://leetcode.com/problems/cyclically-rotating-a-grid/


# Based on Editorial's Approach: Enumerate Each Layer
class Solution:
    def rotateGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        rows, cols = len(grid), len(grid[0])

        for layer in range(min(rows, cols) // 2):
            lo_r, hi_r = layer, rows - layer - 1
            lo_c, hi_c = layer, cols - layer - 1

            # Trace the layer boundary counterclockwise into an ordered list.
            cells: list[tuple[int, int]] = (
                [(i, lo_c) for i in range(lo_r, hi_r)]  # left col ↓
                + [(hi_r, j) for j in range(lo_c, hi_c)]  # bottom row →
                + [(i, hi_c) for i in range(hi_r, lo_r, -1)]  # right col ↑
                + [(lo_r, j) for j in range(hi_c, lo_c, -1)]  # top row ←
            )

            vals = [grid[r][c] for r, c in cells]
            shift = k % len(vals)
            # Cyclic left-shift by `shift`: last `shift` elements move to front.
            rotated = vals[-shift:] + vals[:-shift]
            for (r, c), v in zip(cells, rotated, strict=True):
                grid[r][c] = v

        return grid
