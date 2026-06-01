# 2144. Minimum Cost of Buying Candies With Discount
# https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/


class Solution:
    def minimumCost(self, cost: list[int]) -> int:
        # Greedy: buy from most expensive, so every 3rd candy is free.
        cost.sort(reverse=True)
        return sum(c for i, c in enumerate(cost) if i % 3 != 2)
