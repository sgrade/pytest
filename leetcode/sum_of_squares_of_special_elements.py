# 2778. Sum of Squares of Special Elements
# https://leetcode.com/problems/sum-of-squares-of-special-elements/


class Solution:
    def sumOfSquares(self, nums: list[int]) -> int:
        n = len(nums)
        # Element at 1-based index `index` is special if it divides length.
        return sum(
            nums[index - 1] ** 2 for index in range(1, n + 1) if n % index == 0
        )
