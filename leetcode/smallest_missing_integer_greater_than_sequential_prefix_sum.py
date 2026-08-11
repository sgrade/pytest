# 2996. Smallest Missing Integer Greater Than Sequential Prefix Sum
# https://leetcode.com/problems/smallest-missing-integer-greater-than-sequential-prefix-sum/


class Solution:
    def missingInteger(self, nums: list[int]) -> int:
        sm, i = nums[0], 1
        while i < len(nums):
            if nums[i] - nums[i - 1] == 1:
                sm += nums[i]
                i += 1
            else:
                break

        st = set(nums)
        while sm in st:
            sm += 1
        return sm
