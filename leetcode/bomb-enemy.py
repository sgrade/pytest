# 361. Bomb Enemy
# https://leetcode.com/problems/bomb-enemy/

# Based on Editorial's Approach 2: Dynamic Programming
class Solution:
    def maxKilledEnemies(self, grid: list[list[str]]) -> int:
        if len(grid) == 0:
            return 0
        rows = len(grid)
        cols = len(grid[0])

        row_enemies = 0
        col_enemies = [0] * cols

        ans = 0

        for row in range(rows):
            for col in range(cols):

                if col == 0 or grid[row][col - 1] == 'W':
                    row_enemies = 0
                    for c in range(col, cols):
                        if grid[row][c] == 'W':
                            break
                        elif grid[row][c] == 'E':
                            row_enemies += 1
                
                if row == 0 or grid[row - 1][col] == 'W':
                    col_enemies[col] = 0
                    for r in range(row, rows):
                        if grid[r][col] == 'W':
                            break
                        elif grid[r][col] == 'E':
                            col_enemies[col] += 1
                
                if grid[row][col] == '0':
                    current_ans = row_enemies + col_enemies[col]
                    ans = max(ans, current_ans)
        
        return ans
