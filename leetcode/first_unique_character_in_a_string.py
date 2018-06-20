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

        # https://stackoverflow.com/questions/15495731/best-way-to-find-first-non-repeating-character-in-a-string
        order = list()
        counts = dict()
        for x in s:
            if x in counts:
                counts[x] += 1
            else:
                counts[x] = 1
                order.append(x)
        for x in order:
            if counts[x] == 1:
                return s.index(x)
        return -1

        # One of the solutions based on generators
        # https://stackoverflow.com/questions/15495731/best-way-to-find-first-non-repeating-character-in-a-string
        # Time Limit Exceeded
        """
        try:
            non_repeating_char = next(a for a in s if s.count(a) == 1)
            return s.index(non_repeating_char)
        except StopIteration:
            return -1
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
print(sol.firstUniqChar('llvv'))
