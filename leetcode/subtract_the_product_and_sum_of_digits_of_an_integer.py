# 1281. Subtract the Product and Sum of Digits of an Integer
# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s = str(n)
        sum, product = 0, 1
        for ch in s:
            digit = int(ch)
            sum += digit
            product *= digit
        return product - sum
