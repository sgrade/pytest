# 2110. Number of Smooth Descent Periods of a Stock
# https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/


class Solution:
    def getDescentPeriods(self, prices: list[int]) -> int:
        cur_len, ans = 1, 1
        for i in range(1, len(prices)):
            if prices[i - 1] - prices[i] == 1:
                cur_len += 1
            else:
                cur_len = 1
            ans += cur_len
        return ans
