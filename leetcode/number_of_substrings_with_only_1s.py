# 1513. Number of Substrings With Only 1s
# https://leetcode.com/problems/number-of-substrings-with-only-1s/


class Solution:
    def numSub(self, s: str) -> int:
        MOD = int(1e9 + 7)
        ans, n, ones = 0, len(s), 0
        for i in range(n):
            if s[i] == "0":
                ones = 0
                continue
            ones += 1
            ans += ones
            ans %= MOD
        return ans
