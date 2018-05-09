# https://leetcode.com/problems/contains-duplicate/description/

"""
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
"""


class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        nums_set = set(nums)

        if sorted(nums) != sorted(list(nums_set)):
            return True
        else:
            return False


sol = Solution()
inp = [1,2,3,4]
print(sol.containsDuplicate(inp))
inp = [1,1,1,3,3,4,3,2,4,2]
print(sol.containsDuplicate(inp))
inp = [3, 1]
print(sol.containsDuplicate(inp))
