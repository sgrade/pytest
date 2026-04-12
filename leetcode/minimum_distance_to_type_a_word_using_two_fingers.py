# 1320. Minimum Distance to Type a Word Using Two Fingers
# https://leetcode.com/problems/minimum-distance-to-type-a-word-using-two-fingers/


# Based on Editorials' Approach 1: Dynamic Programming
class Solution:
    def minimumDistance(self, word: str) -> int:
        def cost(a: int, b: int) -> int:
            return abs(a // 6 - b // 6) + abs(a % 6 - b % 6)

        big = 10**9
        base = ord("A")
        # dp[f1][f2] = min cost with fingers at f1, f2; 26 = unplaced.
        dp = [[big] * 27 for _ in range(27)]
        first = ord(word[0]) - base
        dp[first][26] = dp[26][first] = 0

        for ch in word[1:]:
            cur = ord(ch) - base
            ndp = [[big] * 27 for _ in range(27)]
            for f1 in range(27):
                for f2 in range(27):
                    if dp[f1][f2] == big:
                        continue
                    v = dp[f1][f2]
                    # Move finger 1 to cur.
                    c = 0 if f1 == 26 else cost(f1, cur)
                    ndp[cur][f2] = min(ndp[cur][f2], v + c)
                    # Move finger 2 to cur.
                    c = 0 if f2 == 26 else cost(f2, cur)
                    ndp[f1][cur] = min(ndp[f1][cur], v + c)
            dp = ndp

        return min(dp[f1][f2] for f1 in range(27) for f2 in range(27))
