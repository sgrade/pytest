# 3740. Minimum Distance Between Three Equal Elements I
# https://leetcode.com/problems/minimum-distance-between-three-equal-elements-i/

from collections import defaultdict


class Solution:
    def minimumDistance(self, nums: list[int]) -> int:
        # Group indices by value; only the first two matter at any time.
        indices: dict[int, list[int]] = defaultdict(list)
        ans = len(nums) + 1

        for i, v in enumerate(nums):
            indices[v].append(i)
            # Once we have 3+ occurrences, check the latest triple.
            if len(indices[v]) >= 3:
                ans = min(ans, i - indices[v][-3])

        # Distance = sum of pairwise distances = 2 * span.
        return -1 if ans > len(nums) else ans * 2
