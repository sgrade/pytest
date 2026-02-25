# 1356. Sort Integers by The Number of 1 Bits
# https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/


# Based on Editorial's Approach 1: Sort By Custom Comparator: Built-in
class Solution:
    def sortByBits(self, arr: list[int]) -> list[int]:
        arr.sort(key=lambda num: (num.bit_count(), num))
        return arr
