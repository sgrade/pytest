# 26. Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = 0
        for cur in range(1, len(nums)):
            if nums[cur] != nums[prev]:
                nums[prev + 1] = nums[cur]
                prev += 1
        return prev + 1
