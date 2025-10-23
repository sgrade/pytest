# 448. Find All Numbers Disappeared in an Array
# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

from collections import Counter


# Copies the Leetcode's Sample 295 ms submission
class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        cntr = Counter(nums)
        ans = []
        for x in range(1, len(nums) + 1):
            if x not in cntr:
                ans.append(x)
        return ans
