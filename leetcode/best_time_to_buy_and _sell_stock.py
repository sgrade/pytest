# 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        ans = 0
        mn = prices[0]
        for price in prices:
            if price < mn:
                mn = price
            elif price - mn > ans:
                ans = price - mn
        return ans
