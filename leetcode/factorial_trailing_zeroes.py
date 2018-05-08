# https://leetcode.com/problems/factorial-trailing-zeroes/description/

"""
Given an integer n, return the number of trailing zeroes in n!.

Example 1:

Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Note: Your solution should be in logarithmic time complexity.
"""

import math


class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """

        # https://www.geeksforgeeks.org/count-trailing-zeroes-factorial-number/
        count = 0
        i = 5
        while n/i >= 1:
            count += int(n/i)
            i *= 5

        return int(count)

        # Time limit exceeded
        """
        fact = math.factorial(n)
        i = 0
        for x in str(fact)[::-1]:
            if int(x) == 0:
                i += 1
            else:
                break
        return i
        """


sol = Solution()
inp = 8056
print(sol.trailingZeroes(inp))
