# 3903. Smallest Stable Index I
# https://leetcode.com/problems/smallest-stable-index-i/


class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        cur_max, cur_min = nums[0], nums[n - 1]

        mx = [0] * n
        mn = [0] * n
        for i in range(n):
            cur_max = max(cur_max, nums[i])
            mx[i] = cur_max
        for i in range(n - 1, -1, -1):
            cur_min = min(cur_min, nums[i])
            mn[i] = cur_min

        for i in range(n):
            instability_score = mx[i] - mn[i]
            if instability_score <= k:
                return i
        return -1
