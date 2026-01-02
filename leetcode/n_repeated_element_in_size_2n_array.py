# 961. N-Repeated Element in Size 2N Array
# https://leetcode.com/problems/n-repeated-element-in-size-2n-array/


# Based on Editorial's Approach 2: Compare
class Solution:
    def repeatedNTimes(self, nums: list[int]) -> int:
        for diff in range(1, 4):
            for i in range(len(nums) - diff):
                if nums[i] == nums[i + diff]:
                    return nums[i]
        return -1
