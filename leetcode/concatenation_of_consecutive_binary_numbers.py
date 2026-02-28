# 1680. Concatenation of Consecutive Binary Numbers
# https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/

# Based on Editorial's Math (Bitwise Operation)
class Solution:
    def concatenatedBinary(self, n: int) -> int:
        mod = 10**9 + 7
        len, ans = 0, 0
        for i in range(1, n + 1):
            # when meets power of 2, increase the bit length
            if i & (i - 1) == 0:
                len += 1
            ans = ((ans << len) | i) % mod
        return ans
