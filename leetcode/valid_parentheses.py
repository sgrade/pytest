# https://leetcode.com/problems/valid-parentheses/description/

"""Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid. The brackets must close in the correct order,
"()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        correct = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        BRACKETS_MAP = {"[": "]", "{": "}", "(": ")"}

        stack = []
        for bracket in s:
            if bracket in BRACKETS_MAP:
                stack.append(BRACKETS_MAP[bracket])
            elif not stack or bracket != stack.pop():
                return False
        return not stack


x = Solution()
print(x.isValid('([)]'))    # False
print(x.isValid('()[]{}'))  # True
print(x.isValid('([])'))    # True
