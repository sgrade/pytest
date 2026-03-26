# 3548. Equal Sum Grid Partition II
# https://leetcode.com/problems/equal-sum-grid-partition-ii/


# Editorial: Rotation + incremental set (4 passes, one per direction)
class Solution:
    def canPartitionGrid(self, grid: list[list[int]]) -> bool:
        total = sum(v for row in grid for v in row)

        # Rotate the grid 90° clockwise and repeat 4 times so that a single
        # "check horizontal cuts, discard from top" pass covers all four
        # cases: top-heavy horizontal, right-heavy vertical,
        # bottom-heavy horizontal, left-heavy vertical.
        for _ in range(4):
            m, n = len(grid), len(grid[0])
            if m >= 2:
                # exist holds all values seen in rows 0..i so far.
                # Seeding with 0 makes `tag in exist` catch the diff==0 case.
                exist: set[int] = {0}
                top_sum = 0
                for i in range(m - 1):
                    for v in grid[i]:
                        exist.add(v)
                    top_sum += sum(grid[i])
                    # tag > 0  → top is heavier by `tag`; discard from top.
                    # tag == 0 → already balanced.
                    # tag < 0  → bottom is heavier; handled by a later rotation.
                    tag = top_sum * 2 - total

                    if n == 1:
                        # h×1 strip: only the two endpoints are removable.
                        if tag == 0 or tag == grid[0][0] or tag == grid[i][0]:
                            return True
                    elif i == 0:
                        # 1×n strip: only the two endpoints are removable.
                        if tag == 0 or tag in (grid[0][0], grid[0][n - 1]):
                            return True
                    elif tag in exist:
                        # h≥2, n≥2: any cell in the top section is removable.
                        return True

            # 90° clockwise: new[r][c] = old[m-1-c][r]; shape n×m.
            grid = [
                [grid[m - 1 - c][r] for c in range(m)] for r in range(n)
            ]

        return False
