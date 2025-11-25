# 1015. Smallest Integer Divisible by K
# https://leetcode.com/problems/smallest-integer-divisible-by-k/

# Based on Editorial's Smallest Integer Divisible by K
class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        rem = 0
        for n in range(1, k + 1):
            rem = (rem * 10 + 1) % k
            if rem == 0:
                return n
        return -1
