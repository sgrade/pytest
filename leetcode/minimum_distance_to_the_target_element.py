# 1848. Minimum Distance to the Target Element
# https://leetcode.com/problems/minimum-distance-to-the-target-element/


class Solution:
    def getMinDistance(
        self, nums: list[int], target: int, start: int
    ) -> int:
        # Min absolute distance among all indices matching target.
        return min(
            abs(i - start) for i, x in enumerate(nums) if x == target
        )
