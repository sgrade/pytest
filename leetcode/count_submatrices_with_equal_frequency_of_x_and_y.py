# 3212. Count Submatrices With Equal Frequency of X and Y
# https://leetcode.com/problems/count-submatrices-with-equal-frequency-of-x-and-y/


class Solution:
    def numberOfSubmatrices(self, grid: list[list[str]]) -> int:
        # prefix[j] = [X count, Y count] in submatrix (0,0)..(i,j)
        rows, cols = len(grid), len(grid[0])
        prefix = [[0, 0] for _ in range(cols)]
        ans = 0
        for i in range(rows):
            # cx, cy = row-wise running counts for row i
            cx = cy = 0
            for j in range(cols):
                cx += grid[i][j] == "X"
                cy += grid[i][j] == "Y"
                # Accumulate into column prefix to get full 2D prefix sum
                prefix[j][0] += cx
                prefix[j][1] += cy
                if prefix[j][0] > 0 and prefix[j][0] == prefix[j][1]:
                    ans += 1
        return ans
