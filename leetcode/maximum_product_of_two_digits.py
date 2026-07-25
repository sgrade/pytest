# 3536. Maximum Product of Two Digits
# https://leetcode.com/problems/maximum-product-of-two-digits/


class Solution:
    def maxProduct(self, n: int) -> int:
        # Track the two largest digits in one pass instead of sorting.
        top1 = top2 = 0
        for ch in str(n):
            d = int(ch)
            if d > top1:
                top1, top2 = d, top1
            elif d > top2:
                top2 = d
        return top1 * top2
