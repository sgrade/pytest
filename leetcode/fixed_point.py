# 1064. Fixed Point
# https://leetcode.com/problems/fixed-point/


class Solution:
    def fixedPoint(self, arr: list[int]) -> int:
        for num, i in enumerate(arr):
            if num == i:
                return num
        return -1
