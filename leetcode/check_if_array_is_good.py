# 2784. Check if Array is Good
# https://leetcode.com/problems/check-if-array-is-good/


class Solution:
    def isGood(self, nums: list[int]) -> bool:
        nums.sort()
        for i, num in enumerate(nums[:-1]):
            if i + 1 != num:
                return False
        return nums[-1] == len(nums) - 1
