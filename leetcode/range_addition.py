# 370. Range Addition
# https://leetcode.com/problems/range-addition/

"""
You are given an integer length and an array updates where updates[i] = [startIdxi, endIdxi, inci].

You have an array arr of length length with all zeros, and you have some operation to apply on arr. In the ith operation, you should increment all the elements arr[startIdxi], arr[startIdxi + 1], ..., arr[endIdxi] by inci.

Return arr after applying all the updates.
"""


class Solution:
    def getModifiedArray(self, length: int, updates: list[list[int]]) -> list[int]:
        diff_array: list[int] = [0] * (length + 1)
        for interval in updates:
            lo, hi, inc = interval
            diff_array[lo] += inc
            if hi + 1 < length:
                diff_array[hi + 1] -= inc

        ans: list[int] = [0] * length
        ans[0] = diff_array[0]
        for i in range(1, length):
            ans[i] = ans[i - 1] + diff_array[i]
        return ans
