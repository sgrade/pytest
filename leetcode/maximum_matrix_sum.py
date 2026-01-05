# 1975. Maximum Matrix Sum
# https://leetcode.com/problems/maximum-matrix-sum/


class Solution:
    def maxMatrixSum(self, matrix: list[list[int]]) -> int:
        total = 0
        min_abs = 10**9
        negatives = 0
        for row in matrix:
            for num in row:
                cur_abs = abs(num)
                total += cur_abs
                min_abs = min(min_abs, cur_abs)
                if num < 0:
                    negatives += 1
        if negatives % 2 != 0:
            total -= 2 * min_abs
        return total
