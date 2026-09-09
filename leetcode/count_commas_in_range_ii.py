# 3871. Count Commas in Range II
# https://leetcode.com/problems/count-commas-in-range-ii/


class Solution:
    def countCommas(self, n: int) -> int:
        ans = 0
        power = 1000
        while power <= n:
            ans += n - power + 1
            power *= 1000
        return ans
