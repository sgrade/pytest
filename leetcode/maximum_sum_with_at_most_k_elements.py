# 3462. Maximum Sum With at Most K Elements
# https://leetcode.com/problems/maximum-sum-with-at-most-k-elements/

import heapq
from typing import List


class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        sorted_grid = [sorted(row, reverse=True) for row in grid]
        
        largest = []
        for i in range(len(grid)):
            largest.extend(sorted_grid[i][:limits[i]])

        return sum(heapq.nlargest(k, largest))
