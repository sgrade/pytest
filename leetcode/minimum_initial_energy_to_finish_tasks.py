# 1665. Minimum Initial Energy to Finish Tasks
# https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks/


# Based on Editorial's Approach 1: Greedy (Difference Increasing)
class Solution:
    def minimumEffort(self, tasks: list[list[int]]) -> int:
        tasks.sort(key=lambda x: x[1] - x[0])
        ans = 0
        for task in tasks:
            ans = max(ans + task[0], task[1])
        return ans
