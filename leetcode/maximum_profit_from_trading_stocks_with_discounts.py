# 3562. Maximum Profit from Trading Stocks with Discounts
# https://leetcode.com/problems/maximum-profit-from-trading-stocks-with_discounts/
#
# Tree DP + Knapsack: buying a parent stock unlocks 50% discount for its children.
# We track whether discount is available (parent purchased) at each node.


# Based on Editorial's Approach: Tree Dynamic Programming
class Solution:
    def maxProfit(
        self,
        n: int,
        present: list[int],
        future: list[int],
        hierarchy: list[list[int]],
        budget: int,
    ) -> int:
        adj = [[] for _ in range(n)]
        for parent, child in hierarchy:
            adj[parent - 1].append(child - 1)

        def dfs(node: int):
            cost = present[node]
            discounted_cost = cost // 2
            profit = future[node] - cost
            discounted_profit = future[node] - discounted_cost

            # sub_profit[discount_available][spent] = max profit from subtrees only
            sub_profit = [[0] * (budget + 1) for _ in range(2)]
            subtree_size = cost

            # Merge children via knapsack (iterate backwards to avoid reusing items)
            for child in adj[node]:
                child_dp, child_size = dfs(child)
                subtree_size += child_size

                for spent in range(budget, -1, -1):
                    for child_spent in range(min(child_size, spent) + 1):
                        remaining = spent - child_spent
                        for state in (0, 1):
                            sub_profit[state][spent] = max(
                                sub_profit[state][spent],
                                sub_profit[state][remaining]
                                + child_dp[state][child_spent],
                            )

            # dp[parent_purchased][spent] = max profit including this node's decision
            # Base: don't buy this node, children get no discount
            dp = [sub_profit[0][:], sub_profit[0][:]]

            for spent in range(budget + 1):
                # Buy with discount (parent purchased this node) -> children get discount
                if spent >= discounted_cost:
                    dp[1][spent] = max(
                        dp[1][spent],
                        sub_profit[1][spent - discounted_cost] + discounted_profit,
                    )
                # Buy at full price (parent didn't purchase) -> children still get discount
                if spent >= cost:
                    dp[0][spent] = max(
                        dp[0][spent],
                        sub_profit[1][spent - cost] + profit,
                    )

            return dp, subtree_size

        dp, _ = dfs(0)
        return dp[0][budget]  # Root has no parent, so no discount available
