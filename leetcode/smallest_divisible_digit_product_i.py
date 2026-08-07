# 3345. Smallest Divisible Digit Product I
# https://leetcode.com/problems/smallest-divisible-digit-product-i/


class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def digit_product(x: int) -> int:
            product = 1
            while x:
                product *= x % 10
                x //= 10
            return product

        # Scan upward from n until the product of digits is divisible by t.
        while digit_product(n) % t:
            n += 1
        return n
