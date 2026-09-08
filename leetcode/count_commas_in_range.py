# 3870. Count Commas in Range
# https://leetcode.com/problems/count-commas-in-range/


class Solution:
    def countCommas(self, n: int) -> int:
        return max(n - 999, 0)
