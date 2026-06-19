# 1259. Handshakes That Don't Cross
# https://leetcode.com/problems/handshakes-that-dont-cross/


class Solution:
    def numberOfWays(self, numPeople: int) -> int:
        mod = 10**9 + 7
        pairs = numPeople // 2
        # dp[i] = number of non-crossing handshakes
        # for i pairs (Catalan number).
        dp = [1] + [0] * pairs
        for i in range(1, pairs + 1):
            # Pick a partner for person 1; they split the circle into two
            # independent arcs of j pairs and i-1-j pairs.
            for j in range(i):
                dp[i] = (dp[i] + dp[j] * dp[i - 1 - j]) % mod
        return dp[pairs]
