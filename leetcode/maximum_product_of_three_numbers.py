# 628. Maximum Product of Three Numbers
# https://leetcode.com/problems/maximum-product-of-three-numbers/


class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        nums.sort(reverse=True)
        if nums[0] < 0:
            return nums[0] * min(nums[1] * nums[2], nums[-1] * nums[-2])
        return nums[0] * max(nums[1] * nums[2], nums[-1] * nums[-2])
