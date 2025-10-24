# 3462. Maximum Sum With at Most K Elements
# https://leetcode.com/problems/maximum-sum-with-at-most-k-elements/

from typing import List
import heapq


class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        candidates = []
        
        for i, row in enumerate(grid):
            # Get top limits[i] from this row in O(n + limit*log(n))
            top_from_row = heapq.nlargest(limits[i], row)
            candidates.extend(top_from_row)
        
        # Get top k from all candidates in O(total_candidates + k*log(total_candidates))
        return sum(heapq.nlargest(k, candidates))
