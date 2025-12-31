# 1970. Last Day Where You Can Still Cross
# https://leetcode.com/problems/last-day-where-you-can-still-cross/

# Based on Editorial's Approach 3: Disjoint Set Union (on land cells)


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = n  # Number of connected components

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            # Union by rank
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
            self.count -= 1
            return True
        return False


class Solution:
    def latestDayToCross(self, row: int, col: int, cells: list[list[int]]) -> int:
        dsu = UnionFind(row * col + 2)
        grid = [[1] * col for _ in range(row)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for day in range(len(cells) - 1, -1, -1):
            r, c = cells[day][0] - 1, cells[day][1] - 1
            grid[r][c] = 0  # Convert water (1) to land (0) as we go backwards
            idx1 = r * col + c + 1
            for r_diff, c_diff in directions:
                new_r, new_c = r + r_diff, c + c_diff
                idx2 = new_r * col + new_c + 1
                # Only connect to land cells (0), not water cells (1)
                if 0 <= new_r < row and 0 <= new_c < col and grid[new_r][new_c] == 0:
                    dsu.union(idx1, idx2)
            if r == 0:
                dsu.union(0, idx1)
            if r == row - 1:
                dsu.union(row * col + 1, idx1)
            if dsu.find(0) == dsu.find(row * col + 1):
                return day
        return -1
