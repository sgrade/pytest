# 3963. Create Grid With Exactly One Path
# https://leetcode.com/problems/create-grid-with-exactly-one-path/


class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        # The only path: along the top row, then down the last column.
        top = "." * n
        other = "#" * (n - 1) + "."
        return [top] + [other] * (m - 1)
