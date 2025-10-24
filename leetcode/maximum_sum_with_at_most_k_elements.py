# 3462. Maximum Sum With at Most K Elements
# https://leetcode.com/problems/maximum-sum-with-at-most-k-elements/

from typing import List


class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:       
        largest = []
        for i in range(len(grid)):
            sorted_row = sorted(grid[i], reverse=True)
            largest.extend(sorted_row[:limits[i]])
        largest.sort(reverse=True)
        return sum(largest[:k])
