# 1458. Max Dot Product of Two Subsequences
# https://leetcode.com/problems/max-dot-product-of-two-subsequences/


# Based on Editorial's Approach 1: Top-Down Dynamic Programming
class Solution:
    def maxDotProduct(self, nums1: list[int], nums2: list[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        SENTINEL = -(10**18)
        memo = [[SENTINEL] * n2 for _ in range(n1)]

        def get_product(idx1, idx2):
            if idx1 == n1 or idx2 == n2:
                return 0
            if memo[idx1][idx2] != SENTINEL:
                return memo[idx1][idx2]

            take_both = nums1[idx1] * nums2[idx2]
            move_both = take_both + get_product(idx1 + 1, idx2 + 1)
            move_idx1 = get_product(idx1 + 1, idx2)
            move_idx2 = get_product(idx1, idx2 + 1)
            memo[idx1][idx2] = max(move_both, move_idx1, move_idx2)
            return memo[idx1][idx2]

        mn1, mx1 = min(nums1), max(nums1)
        mn2, mx2 = min(nums2), max(nums2)
        if mx1 < 0 and mn2 > 0:
            return mx1 * mn2
        if mx2 < 0 and mn1 > 0:
            return mx2 * mn1

        return get_product(0, 0)
