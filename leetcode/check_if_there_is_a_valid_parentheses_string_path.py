# 2267. Check if There Is a Valid Parentheses String Path
# https://leetcode.com/problems/check-if-there-is-a-valid-parentheses-string-path/


# Based on Editorial's Approach: Dynamic Programming
class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        rows, cols = len(grid), len(grid[0])

        # A valid string needs even length, must open first and close last.
        if (rows + cols - 1) % 2 == 1:
            return False
        if grid[0][0] != "(" or grid[-1][-1] != ")":
            return False

        # balances[r][c] is a bitmask: bit k is set if some path to (r, c)
        # has balance k (open minus close count).
        balances = [[0] * cols for _ in range(rows)]
        balances[0][0] = 1 << 1  # After the first "(" the balance is 1.

        for r in range(rows):
            for c in range(cols):
                if r == 0 and c == 0:
                    continue
                incoming = 0
                if r > 0:
                    incoming |= balances[r - 1][c]
                if c > 0:
                    incoming |= balances[r][c - 1]
                # "(" increments every balance; ")" decrements it, and the
                # right shift drops balance 0, which would go negative.
                if grid[r][c] == "(":
                    balances[r][c] = incoming << 1
                else:
                    balances[r][c] = incoming >> 1

        # Valid if some path ends with balance 0.
        return bool(balances[-1][-1] & 1)
