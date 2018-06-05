# https://leetcode.com/problems/power-of-three/description/

"""
Given an integer, write a function to determine if it is a power of three.

Example 1:

Input: 27
Output: true
Example 2:

Input: 0
Output: false
Example 3:

Input: 9
Output: true
Example 4:

Input: 45
Output: false
Follow up:
Could you do it without using any loop / recursion?
"""


class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """

        # https://leetcode.com/problems/power-of-three/solution/
        # Integer Limitations [Accepted]
        # Your runtime beats 62.23 % of python3 submissions.
        return n > 0 and 1162261467 % n == 0


sol = Solution()
inp = 45
print(sol.isPowerOfThree(inp))
