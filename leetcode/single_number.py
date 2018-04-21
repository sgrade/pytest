from datetime import datetime
# https://leetcode.com/problems/single-number/description/

"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
"""

startTime = datetime.now()
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # https://leetcode.com/problems/single-number/solution/
        return 2 * sum(set(nums)) - sum(nums)

        """
        # time is bad: 
        while nums:
            candidate = nums[-1]
            nums.pop()
            try:
                nums.remove(candidate)
            except:
                return candidate
        """

print(datetime.now() - startTime)


sol = Solution()
# inp = [2,2,1]
inp = [4,1,2,1,2]
print(sol.singleNumber(inp))