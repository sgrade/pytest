# 1391. Check if There is a Valid Path in a Grid
# https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/


# Based on Editorial's Approach: Constructing a Graph Based on Cell Property
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            x, y = y, x
        self.parent[y] = x
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1


class Solution:
    def hasValidPath(self, grid: list[list[int]]) -> bool:
        rows, cols = len(grid), len(grid[0])
        # Bitmask for each street type: bits 0-3 = N, E, S, W
        patterns = [0, 0b1010, 0b0101, 0b1100, 0b0110, 0b1001, 0b0011]
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        uf = UnionFind(rows * cols)

        for x in range(rows):
            for y in range(cols):
                pattern = patterns[grid[x][y]]
                for i, (dx, dy) in enumerate(dirs):
                    if not (pattern & (1 << i)):
                        continue
                    sx, sy = x + dx, y + dy
                    # Neighbour must connect back via the opposite direction
                    if (
                        0 <= sx < rows
                        and 0 <= sy < cols
                        and (patterns[grid[sx][sy]] & (1 << ((i + 2) % 4)))
                    ):
                        uf.union(x * cols + y, sx * cols + sy)

        return uf.find(0) == uf.find((rows - 1) * cols + (cols - 1))
