# 2089. Find Target Indices After Sorting Array
# https://leetcode.com/problems/find-target-indices-after-sorting-array/


class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        return [t[0] for t in list(enumerate(sorted(nums))) if t[1] == target]
