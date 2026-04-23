# 2615. Sum of Distances
# https://leetcode.com/problems/sum-of-distances/

from collections import defaultdict


# Based on Editorial's Approach: Grouping + Prefix Sum
class Solution:
    def distance(self, nums: list[int]) -> list[int]:
        # Group indices by value; only equal values contribute to each other.
        groups = defaultdict(list)
        for i, v in enumerate(nums):
            groups[v].append(i)

        ans = [0] * len(nums)
        for group in groups.values():
            # For the j-th index `idx` in a group of size `sz` with index sum
            # `total`, the distance sum simplifies to:
            #   (2*j - sz) * idx + total - 2 * prefix.
            total, sz = sum(group), len(group)
            prefix = 0
            for j, idx in enumerate(group):
                ans[idx] = (2 * j - sz) * idx + total - 2 * prefix
                prefix += idx
        return ans
