# https://leetcode.com/problems/reverse-integer/description/

# Given a 32-bit signed x, reverse digits of an x.


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # https://en.wikipedia.org/wiki/32-bit
        max_integer = 2 ** 31

        if x < 0:
            positive_integer = str(x).lstrip('-')
            stringed = '-' + str(positive_integer)[::-1]
        else:
            stringed = str(x)[::-1]

        result = int(stringed)

        if -max_integer <= result <= (max_integer - 1):
            return result
        else:
            return 0


tst = Solution()
print(tst.reverse(-1534236469))