# 3286. Find a Safe Walk Through a Grid
# https://leetcode.com/problems/find-a-safe-walk-through-a-grid/

import heapq


# Based on Editorial's Approach 1: Dijkstra
class Solution:
    def findSafeWalk(self, grid: list[list[int]], health: int) -> bool:
        rows, cols = len(grid), len(grid[0])
        cost = [[-1] * cols for _ in range(rows)]
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        pq = [(grid[0][0], 0, 0)]
        while pq:
            cur_cost, cur_row, cur_col = heapq.heappop(pq)
            if cost[cur_row][cur_col] >= 0:
                continue
            cost[cur_row][cur_col] = cur_cost
            for diff_r, diff_c in directions:
                r, c = cur_row + diff_r, cur_col + diff_c
                if 0 <= r < rows and 0 <= c < cols and cost[r][c] == -1:
                    heapq.heappush(pq, (cur_cost + grid[r][c], r, c))
        return cost[rows - 1][cols - 1] < health
