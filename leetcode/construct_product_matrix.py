# 2906. Construct Product Matrix
# https://leetcode.com/problems/construct-product-matrix/

# Based on Editorial's Approach: Suffix Product
class Solution:
    def constructProductMatrix(self, grid: list[list[int]]) -> list[list[int]]:
        mod = 12345
        rows, cols = len(grid), len(grid[0])
        product = [[0] * cols for _ in range(rows)]

        suffix = 1
        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                product[i][j] = suffix
                suffix = (suffix * grid[i][j]) % mod

        prefix = 1
        for i in range(rows):
            for j in range(cols):
                product[i][j] = (product[i][j] * prefix) % mod
                prefix = (prefix * grid[i][j]) % mod

        return product
