# 1569. Number of Ways to Reorder Array to Get Same BST
# https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/

from math import comb

MOD = 10**9 + 7


# Based on Editorial's Approach: Recursion
class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        def count_orders(values: list[int]) -> int:
            """Counts orderings of `values` that build the same BST."""
            if len(values) < 3:
                return 1
            root = values[0]
            left = [v for v in values if v < root]
            right = [v for v in values if v > root]
            # Interleave the left and right subsequences in any way while
            # keeping each one's relative order: C(n - 1, len(left)) ways.
            interleavings = comb(len(values) - 1, len(left))
            return (
                interleavings * count_orders(left) * count_orders(right) % MOD
            )

        # Exclude the original ordering itself.
        return (count_orders(nums) - 1) % MOD
