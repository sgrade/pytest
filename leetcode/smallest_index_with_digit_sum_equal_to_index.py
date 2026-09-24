# 3550. Smallest Index With Digit Sum Equal to Index
# https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/


class Solution:
    def smallestIndex(self, nums: list[int]) -> int:
        def digit_sum(num: int) -> int:
            total = 0
            while num:
                total += num % 10
                num //= 10
            return total

        # Return the first index whose value has a matching digit sum.
        for index, num in enumerate(nums):
            if digit_sum(num) == index:
                return index
        return -1
