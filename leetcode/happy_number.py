# https://leetcode.com/problems/happy-number/description/

"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example:

Input: 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""


class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        def square_digits(digit):
            sum = 0
            for x in str(digit):
                sum += int(x) * int(x)
            return sum

        output = n


        i = 0
        while i < 100:
            output = square_digits(output)
            if output == 1:
                return True
            else:
                i += 1

        return False


sol = Solution()
inp = 2
print(sol.isHappy(inp))
