# 3727. Maximum Alternating Sum of Squares
# https://leetcode.com/problems/maximum-alternating-sum-of-squares/


class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        # Rearranging is free, so put the largest squares at the positive
        # (even) positions and the smallest at the negative (odd) ones.
        squares = sorted(num * num for num in nums)
        half = len(nums) // 2
        # The smallest n // 2 squares are subtracted, the rest are added.
        return sum(squares[half:]) - sum(squares[:half])
