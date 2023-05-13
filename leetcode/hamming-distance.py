# 461. Hamming Distance
# https://leetcode.com/problems/hamming-distance/

# From Editorial's Approach 3: Brian Kernighan's Algorithm
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        ans = 0
        while xor:
            ans += 1
            xor = xor & (xor - 1)
        return ans
