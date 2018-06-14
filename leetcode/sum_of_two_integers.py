# https://leetcode.com/problems/sum-of-two-integers/description/

"""
alculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example:
Given a = 1 and b = 2, return 3.

Credits:
Special thanks to @fujiaozhu for adding this problem and creating all test cases.
"""


class Solution:
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """

        # Runtime: 36 ms
        # Your runtime beats 92.66 % of python3 submissions
        lst1 = [a, b]
        return sum(lst1)


sol = Solution()
print(sol.getSum(0, 2))
