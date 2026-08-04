# 3731. Find Missing Elements
# https://leetcode.com/problems/find-missing-elements/


class Solution:
    def findMissingElements(self, nums: list[int]) -> list[int]:
        # After sorting, missing values are the integers strictly between
        # each consecutive pair.
        nums.sort()
        ans = []
        for i in range(len(nums) - 1):
            ans.extend(range(nums[i] + 1, nums[i + 1]))
        return ans
