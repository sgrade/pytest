# 3727. Maximum Alternating Sum of Squares
# https://leetcode.com/problems/maximum-alternating-sum-of-squares/


class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        n = len(nums)
        squares = [num**2 for num in nums]
        squares.sort(reverse=True)
        score = 0
        for i in range(n // 2):
            score += squares[i]
            score -= squares[n - i - 1]
        if n % 2 != 0:
            score += squares[n // 2]
        return score
