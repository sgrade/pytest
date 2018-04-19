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

        def get_max_profit(prs, min_pr):
            # If not initialized, max_pr might be referenced before assignment
            # print('prs:', prs)
            max_pr = 0
            while prs:
                # print('min_pr:', min_pr, 'index:', prs.index(min_pr))
                max_pr = max(prs)
                # print('max_pr:', max_pr, 'index:', prs.index(max_pr))
                if prs.index(max_pr) > prs.index(min_pr):
                    # print('found max profit')
                    break
                else:
                    # print('executing else:')
                    prs.remove(max_pr)
            # print('returning', max_pr, '-', min_pr)
            return max_pr - min_pr

        max_profit = 0
        while prices:
            min_price = min(prices)
            profit = get_max_profit(prices[:], min_price)
            if profit > max_profit:
                max_profit = profit
                # print('profit id', id(profit))
                # print('max_profit id', id(max_profit))
            prices.remove(min_price)
        else:
            return max_profit


sol = Solution()
# inp = [7, 1, 5, 3, 6, 4]    # Expected: 5
# inp = [7, 6, 4, 3, 1]    # Expected: 0
# inp = [7, 1, 6, 3, 2]    # Expected: 5
# inp = []    # Expected: 0
# inp = [2, 4, 1]    # Expected: 2
# inp = [4, 1, 2]    # Expected: 1
# inp = [3, 2, 6, 5, 0, 3]     # Expected: 4
print(sol.maxProfit(inp))
