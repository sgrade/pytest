# https://leetcode.com/problems/first-unique-character-in-a-string/description/

"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
"""


class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        # Time Limit Exceeded
        """
        for char in s:
            if s.count(char) == 1:
                return s.index(char)

        return -1
        """


sol = Solution()
print(sol.firstUniqChar('leetcode'))
print(sol.firstUniqChar('loveleetcode'))