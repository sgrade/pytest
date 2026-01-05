# 1975. Maximum Matrix Sum
# https://leetcode.com/problems/maximum-matrix-sum/


class Solution:
    def maxMatrixSum(self, matrix: list[list[int]]) -> int:
        total = 0
        min_abs = 10**9
        negatives, zeroes = 0, 0
        for row in matrix:
            for num in row:
                if num < 0:
                    negatives += 1
                    cur_abs = abs(num)
                    min_abs = min(min_abs, cur_abs)
                    total += cur_abs
                elif num > 0:
                    total += num
                    min_abs = min(min_abs, num)
                else:
                    zeroes += 1
        if zeroes == 0 and negatives % 2 != 0:
            total -= 2 * min_abs
        return total
