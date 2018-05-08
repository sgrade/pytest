# https://leetcode.com/problems/majority-element/description/

"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.
"""

import collections


class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # https://leetcode.com/problems/majority-element/solution/
        # Approach #2 HashMap [Accepted]

        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)

        """
        # Submission Result: Time Limit Exceeded
        nums_length = len(nums)

        for element in nums:
            number_of_appearances = nums.count(element)
            if number_of_appearances > nums_length / 2:
                return element
        """


sol = Solution()
inp = [1, 2, 3, 4, 1, 4, 1, 1, 2, 1, 1]
print(sol.majorityElement(inp))
