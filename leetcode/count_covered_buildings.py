# 3531. Count Covered Buildings
# https://leetcode.com/problems/count-covered-buildings/


# Based on Editorial's Approach: Simulation
class Solution:
    def countCoveredBuildings(self, n: int, buildings: list[list[int]]) -> int:
        min_col_in_row = [n + 1] * (n + 1)
        max_col_in_row = [0] * (n + 1)
        min_row_in_col = [n + 1] * (n + 1)
        max_row_in_col = [0] * (n + 1)

        for building in buildings:
            r, c = building[0], building[1]
            min_col_in_row[r] = min(c, min_col_in_row[r])
            max_col_in_row[r] = max(c, max_col_in_row[r])
            min_row_in_col[c] = min(r, min_row_in_col[c])
            max_row_in_col[c] = max(r, max_row_in_col[c])

        ans = 0
        for building in buildings:
            r, c = building[0], building[1]
            if (
                r > min_row_in_col[c]
                and r < max_row_in_col[c]
                and c > min_col_in_row[r]
                and c < max_col_in_row[r]
            ):
                ans += 1
        return ans
