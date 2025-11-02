# 1183. Maximum Number of Ones
# https://leetcode.com/problems/maximum-number-of-ones/


# Based on Editorial's Approach 1: Greedy
class Solution:
    def maximumNumberOfOnes(
        self, width: int, height: int, sideLength: int, maxOnes: int
    ) -> int:
        max_ones = []
        # Check each cell in the top-left window of size sideLength x sideLength
        for row in range(sideLength):
            for col in range(sideLength):
                max_ones_in_column = 1 + (width - col - 1) // sideLength
                max_ones_in_row = 1 + (height - row - 1) // sideLength
                cur_max_ones = max_ones_in_column * max_ones_in_row
                max_ones.append(cur_max_ones)
        max_ones.sort(reverse=True)
        return sum(max_ones[:maxOnes])
