# https://leetcode.com/problems/missing-number/description/

"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
"""

class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        """
        Your runtime beats 27.85 % of python3 submissions
        nums.sort()
        # Check if 0 is the missing number
        if nums[0] != 0:
            return 0
        if nums[-1] != len(nums):
            return len(nums)

        i = 0
        while i != len(nums):
            if i != nums[i]:
                return i
            i += 1
        """

        """
        # https://leetcode.com/problems/missing-number/solution/
        # Approach #2 HashSet [Accepted]
        # "Your runtime beats 19.75 % of python3 submissions."
        nums_set = set(nums)
        for number in range(len(nums) + 1):
            if number not in nums_set:
                return number
        """
        """
        #  "Time Limit Exceeded"
        for number in range(len(nums) + 1):
            if number not in nums:
                return number
        """


sol = Solution()
# inp = [3,0,1]
# inp = [9,6,4,2,3,5,7,0,1]
# inp = [0] # expected 1
inp = [0, 1]    # expected 2
print(sol.missingNumber(inp))
