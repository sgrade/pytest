# 3963. Create Grid With Exactly One Path
# https://leetcode.com/problems/create-grid-with-exactly-one-path/


class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        ans = [["#"] * n for _ in range(m)]
        for c in range(n):
            ans[0][c] = "."
        for r in range(m):
            ans[r][n - 1] = "."
        ans = ["".join(ans[r]) for r in range(m)]
        return ans
