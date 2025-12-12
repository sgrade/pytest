# 1874. Minimize Product Sum of Two Arrays
# https://leetcode.com/problems/minimize-product-sum-of-two-arrays/


class Solution:
    def minProductSum(self, nums1: list[int], nums2: list[int]) -> int:
        nums1.sort()
        nums2.sort(reverse=True)
        product_sum = 0
        for i in range(len(nums1)):
            product_sum += nums1[i] * nums2[i]
        return product_sum
