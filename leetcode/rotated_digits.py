# 788. Rotated Digits
# https://leetcode.com/problems/rotated-digits/


from functools import cache


# Based on Editorial's Approach: Dynamic Programming
class Solution:
    def rotatedDigits(self, n: int) -> int:
        # Digit DP over decimal digits of n. tight: prefix equals n so far.
        # has_diff: some digit in {2,5,6,9}, so rotated number differs.
        digits = tuple(map(int, str(n)))
        invalid = frozenset({3, 4, 7})
        good = frozenset({2, 5, 6, 9})

        @cache
        def dp(i: int, tight: bool, has_diff: bool) -> int:
            if i == len(digits):
                return int(has_diff)
            limit = digits[i] if tight else 9
            total = 0
            for d in range(limit + 1):
                if d in invalid:
                    continue
                total += dp(
                    i + 1,
                    tight and d == digits[i],
                    has_diff or d in good,
                )
            return total

        return dp(0, True, False)
