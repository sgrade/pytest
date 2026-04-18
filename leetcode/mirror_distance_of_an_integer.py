# 3783. Mirror Distance of an Integer
# https://leetcode.com/problems/mirror-distance-of-an-integer/


class Solution:
    def mirrorDistance(self, n: int) -> int:
        tmp, reversed = n, 0
        while tmp:
            reversed = reversed * 10 + tmp % 10
            tmp //= 10
        return abs(n - reversed)
