# 1621. Number of Sets of K Non-Overlapping Line Segments
# https://leetcode.com/problems/number-of-sets-of-k-non-overlapping-line-segments/


import math


# Based on Editorial's Approach 2: Combinatorics
class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        return math.comb(n + k - 1, k * 2) % (10**9 + 7)
