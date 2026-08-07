# 3348. Smallest Divisible Digit Product II
# https://leetcode.com/problems/smallest-divisible-digit-product-ii/

import math


# Based on Editorial's Approach: Enumerate the String from Right to Left
class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        # A digit product only carries the primes 2, 3, 5 and 7, so t must
        # factor completely into digits 2..9.
        # If t has any other prime factor (11, 13, 17, …), no such product
        # can be divisible by t, so the answer is "-1"
        leftover = t
        for digit in range(2, 10):
            while leftover % digit == 0:
                leftover //= digit
        if leftover > 1:
            return "-1"

        n = len(num)
        digits = list(num)

        # missing[i] = part of t not yet covered by the prefix num[:i].
        # A '0' kills the product, so no prefix may reach past it.
        missing = [t] + [0] * n
        last_bumpable = n - 1
        for i, digit in enumerate(digits):
            if digit == "0":
                last_bumpable = i
                break
            missing[i + 1] = missing[i] // math.gcd(missing[i], int(digit))

        # num already works.
        if missing[n] == 1:
            return num

        # Otherwise keep the length: raise one digit and rebuild the suffix.
        # Scanning right to left returns the smallest such number.
        for i in range(last_bumpable, -1, -1):
            for bumped in range(int(digits[i]) + 1, 10):
                digits[i] = str(bumped)
                rest = missing[i] // math.gcd(missing[i], bumped)
                # Greedily push the biggest factors to the rightmost slots so
                # the leading slots stay '1' (largest usable digit only
                # shrinks, hence the shared counter).
                largest = 9
                for j in range(n - 1, i, -1):
                    while rest % largest:
                        largest -= 1
                    rest //= largest
                    digits[j] = str(largest)
                if rest == 1:
                    return "".join(digits)

        # No answer of the same length: use n + 1 digits, factoring t into
        # as few digits as possible and padding the front with '1'.
        factors = []
        rest = t
        for digit in range(9, 1, -1):
            while rest % digit == 0:
                factors.append(str(digit))
                rest //= digit
        factors.reverse()  # Ascending digits give the smallest number.
        padding = "1" * max(n + 1 - len(factors), 0)
        return padding + "".join(factors)
