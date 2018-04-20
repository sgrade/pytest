# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/

"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.
"""


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        # solution is "Approach #2 (Peak Valley Approach)" from here
        # https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/solution/
        # translated from Java to Python

        i = 0
        max_profit = 0
        prices_length = len(prices)

        while i < prices_length - 1:

            while i < prices_length - 1 and prices[i] >= prices[i + 1]:
                i += 1
            valley = prices[i]
            # print('valley:', valley)

            while i < prices_length - 1 and prices[i] <= prices[i + 1]:
                i += 1
            peak = prices[i]
            # print('peak:', peak)

            max_profit += peak - valley
            # print(max_profit)

        return max_profit


sol = Solution()
# inp = []  # Expected: 0
# inp = [7,1,5,3,6,4]    # Expected: 7
# inp = [1,2,3,4,5]    # Expected: 4
# inp = [7,6,4,3,1]    # Expected: 0
inp = [7,1,5,9,6,4]
print(sol.maxProfit(inp))
