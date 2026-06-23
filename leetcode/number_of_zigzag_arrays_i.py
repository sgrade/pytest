# 3699. Number of ZigZag Arrays I
# https://leetcode.com/problems/number-of-zigzag-arrays-i/

from itertools import accumulate


# Based on Editorial's Approach: Dynamic Programming + Prefix Sum Optimization
class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        mod = 10**9 + 7
        m = r - l + 1

        # dp[v]: zigzag arrays of the current length ending at the v-th value
        # with the last step going down. The "up" case is the mirror image
        # (dp reversed), so tracking one array suffices.
        dp = [1] * m
        for _ in range(n - 1):
            # A new down-step value can follow any larger up-step value, i.e.
            # a prefix sum over the mirrored (reversed) dp.
            prefix = accumulate(reversed(dp), initial=0)
            dp = [next(prefix) % mod for _ in range(m)]

        # Total = down-ending + up-ending arrays = 2 * sum(dp).
        return 2 * sum(dp) % mod
