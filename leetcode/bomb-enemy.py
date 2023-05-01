# 361. Bomb Enemy
# https://leetcode.com/problems/bomb-enemy/

# Optimized with Leetcode's Python Sample 615 ms submission
class Solution:
    def maxKilledEnemies(self, grid) -> int:
        if len(grid) == 0:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        ans = 0

        for row in range(rows):
            grid[row].append('W')
        grid.append(['W'] * (cols + 1))

        for row in grid:
            enemies = 0
            empty_cells = []
            for idx in range(cols + 1):
                if row[idx] == 'E':
                    enemies += 1
                elif row[idx] == 'W':
                    for i in empty_cells:
                        row[i] = enemies
                    enemies = 0
                    empty_cells = []
                else:
                    empty_cells.append(idx)

        for col in range(cols):
            enemies = 0
            empty_cells = []
            for row in range(rows + 1):
                if grid[row][col] == 'E':
                    enemies += 1
                elif grid[row][col] == 'W':
                    for i in empty_cells:
                        grid[i][col] += enemies
                        ans = max(ans, grid[i][col])
                    enemies = 0
                    empty_cells = []
                else:
                    empty_cells.append(row)
        
        return ans
