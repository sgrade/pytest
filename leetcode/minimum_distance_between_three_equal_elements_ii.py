# 3741. Minimum Distance Between Three Equal Elements II
# https://leetcode.com/problems/minimum-distance-between-three-equal-elements-ii/

from collections import defaultdict


class Solution:
    def minimumDistance(self, nums: list[int]) -> int:
        # Track indices per value; check the latest triple on the fly.
        indices: dict[int, list[int]] = defaultdict(list)
        ans = len(nums) + 1

        for i, v in enumerate(nums):
            indices[v].append(i)
            if len(indices[v]) >= 3:
                ans = min(ans, i - indices[v][-3])

        return -1 if ans > len(nums) else ans * 2
