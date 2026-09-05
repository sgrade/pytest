# 3904. Smallest Stable Index II
# https://leetcode.com/problems/smallest-stable-index-ii/


class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)

        # suffix_min[i] is the minimum of nums[i:].
        suffix_min = [0] * n
        cur_min = nums[-1]
        for i in range(n - 1, -1, -1):
            cur_min = min(cur_min, nums[i])
            suffix_min[i] = cur_min

        # Sweep left to right, tracking the maximum of nums[:i + 1].
        cur_max = nums[0]
        for i, num in enumerate(nums):
            cur_max = max(cur_max, num)
            if cur_max - suffix_min[i] <= k:
                return i
        return -1
