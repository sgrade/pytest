# 167. Two Sum II - Input Array Is Sorted
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        lo, hi = 0, len(numbers) - 1
        while lo < hi:
            sum = numbers[lo] + numbers[hi]
            if sum == target:
                return [lo + 1, hi + 1]
            elif sum > target:
                hi -= 1
            else:
                lo += 1
        return [-1, -1]
