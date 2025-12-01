# 2141. Maximum Running Time of N Computers
# https://leetcode.com/problems/maximum-running-time-of-n-computers/


# Based on Editorial's Approach 1: Sorting and Prefix Sum
class Solution:
    def maxRunTime(self, n: int, batteries: list[int]) -> int:
        batteries.sort()
        shared = sum(batteries[:-n])

        n_largest = batteries[-n:]

        for i in range(n - 1):
            need = n_largest[i + 1] - n_largest[i]
            if shared // (i + 1) < need:
                have = shared // (i + 1)
                return n_largest[i] + have
            shared -= (i + 1) * need

        return n_largest[-1] + shared // n
