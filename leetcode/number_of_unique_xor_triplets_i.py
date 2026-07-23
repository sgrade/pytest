# 3513. Number of Unique XOR Triplets I
# https://leetcode.com/problems/number-of-unique-xor-triplets-i/

# Based on Editorial's Approach: Find the Pattern
class Solution:
    def uniqueXorTriplets(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        ans = 1
        while ans <= n:
            ans <<= 1
        return ans
