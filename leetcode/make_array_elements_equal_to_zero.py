# 3354. Make Array Elements Equal to Zero
# https://leetcode.com/problems/make-array-elements-equal-to-zero/

from typing import List


# Based on Editorial's Approach 2: Prefix Sum
class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        n, ans = len(nums), 0
        sm = sum(nums)
        left, right = 0, sm
        for i in range(n):
            if nums[i] == 0:
                if 0 <= left - right <= 1:
                    ans += 1
                if 0 <= right - left <= 1:
                    ans += 1
            else:
                left += nums[i]
                right -= nums[i]
        return ans
