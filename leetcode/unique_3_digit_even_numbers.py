# 3483. Unique 3-Digit Even Numbers
# https://leetcode.com/problems/unique-3-digit-even-numbers/

import itertools


class Solution:
    def totalNumbers(self, digits: list[int]) -> int:
        # A set removes duplicates caused by repeated input digits.
        numbers = {
            100 * hundreds + 10 * tens + ones
            for hundreds, tens, ones in itertools.permutations(digits, 3)
            if hundreds != 0 and ones % 2 == 0
        }
        return len(numbers)
