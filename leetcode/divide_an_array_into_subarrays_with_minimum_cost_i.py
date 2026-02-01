# 3010. Divide an Array Into Subarrays With Minimum Cost I
# https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-i/


class Solution:
    def minimumCost(self, nums: list[int]) -> int:
        mins = [nums[1], nums[2]]
        mins.sort()
        for i in range(3, len(nums)):
            if nums[i] < mins[1]:
                mins[1] = nums[i]
            mins.sort()
        cost = nums[0] + mins[0] + mins[1]
        return cost
