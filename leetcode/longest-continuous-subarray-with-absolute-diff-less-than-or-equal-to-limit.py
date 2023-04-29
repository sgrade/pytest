# 1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
# https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

from collections import deque

class Solution:
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        left = 0
        maxq = deque()
        minq = deque()
        right = 0
        while right < len(nums):
            while minq and minq[-1] > nums[right]:
                minq.pop()
            minq.append(nums[right])
            while maxq and maxq[-1] < nums[right]:
                maxq.pop()
            maxq.append(nums[right])
            if maxq[0] - minq[0] > limit:
                if minq[0] == nums[left]:
                    minq.popleft()
                if maxq[0] == nums[left]:
                    maxq.popleft()
                left += 1
            right += 1
        return right - left
