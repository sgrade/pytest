# https://leetcode.com/problems/valid-palindrome/description/

"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
"""


class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        s_forward = [word.lower() for word in s if word.isalnum()]
        # print(s_forward)
        s_backward = [word.lower() for word in s[::-1] if word.isalnum()]
        # print(s_backward)
        if s_forward == s_backward:
            return True
        else:
            return False

sol = Solution()
# inp = "A man, a plan, a canal: Panama"
# inp = "race a car"
inp = ""
print(sol.isPalindrome(inp))
