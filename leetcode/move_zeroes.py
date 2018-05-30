# https://leetcode.com/problems/move-zeroes/description/

"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""


class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # Runtime: 112 ms
        # Your runtime beats 26.76 % of python3 submissions.
        i = 0
        while True:
            try:
                nums.remove(0)
                i += 1
            except ValueError:
                while i > 0:
                    nums.append(0)
                    i -= 1
                print(nums)
                break


sol = Solution()
inp = [0, 1, 0, 3, 12]
sol.moveZeroes(inp)
