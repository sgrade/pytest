# 1855. Maximum Distance Between a Pair of Values
# https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/


class Solution:
    def maxDistance(self, nums1: list[int], nums2: list[int]) -> int:
        ans = 0
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                i += 1
            else:
                ans = max(ans, j - i)
                j += 1
        return ans
