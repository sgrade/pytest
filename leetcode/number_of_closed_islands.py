# 1254. Number of Closed Islands
# https://leetcode.com/problems/number-of-closed-islands/

from collections import deque


class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        closed_islands = 0

        directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]

        def bfs(start_r: int, start_c: int):
            q = deque([(start_r, start_c)])
            visited[start_r][start_c] = True
            is_closed = True

            while q:
                cur_r, cur_c = q.popleft()
                for r_diff, c_diff in directions:
                    r = cur_r + r_diff
                    c = cur_c + c_diff
                    if r < 0 or r >= rows or c < 0 or c >= cols:
                        is_closed = False
                    elif grid[r][c] == 0 and not visited[r][c]:
                        q.append((r, c))
                        visited[r][c] = True
            return is_closed

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0 and not visited[r][c] and bfs(r, c):
                    closed_islands += 1
        return closed_islands
