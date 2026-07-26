# 628. Maximum Product of Three Numbers
# https://leetcode.com/problems/maximum-product-of-three-numbers/


class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        mx: list = [-1000, -1000, -1000]
        mn: list = [1000, 1000]
        for num in nums:
            if num > mx[0]:
                mx.append(num)
                mx.sort()
                mx = mx[1:]
            if num < mn[1]:
                mn.append(num)
                mn.sort()
                mn = mn[:2]
        return max(mx[-1] * mx[-2] * mx[-3], mx[-1] * mn[0] * mn[1])
