# 3751. Total Waviness of Numbers in Range I
# https://leetcode.com/problems/total-waviness-of-numbers-in-range-i/


# Based on Editorial's Approach 1: Enumeration
class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def waviness(n: int) -> int:
            s = str(n)
            # count local peaks (a < b > c) and local valleys (a > b < c)
            return sum(
                (a < b > c) or (a > b < c)
                for a, b, c in zip(s, s[1:], s[2:], strict=True)
            )

        return sum(waviness(n) for n in range(num1, num2 + 1))
