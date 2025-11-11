# 474. Ones and Zeroes
# https://leetcode.com/problems/ones-and-zeroes/

from typing import List


# Based on Editorial's Approach #5 Dynamic Programming
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for s in strs:
            zeroes = s.count("0")
            ones = len(s) - zeroes
            for z in range(m, zeroes - 1, -1):
                for o in range(n, ones - 1, -1):
                    dp[z][o] = max(1 + dp[z - zeroes][o - ones], dp[z][o])
        return dp[m][n]
