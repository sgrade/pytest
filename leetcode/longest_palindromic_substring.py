# https://leetcode.com/problems/longest-palindromic-substring/description/

"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        # Time Limit Exceeded
        """
        def check_palindrome(string):
            if string[::-1] == string:
                return True
            else:
                return False

        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return s
        else:

            s_length = len(s)
            longest_pal = s[0]  # To store the result
            longest_pal_length = 1
            for i in range(0, s_length):
                for j in range(1, s_length+1):
                    # print('checking', s[i:j])
                    if check_palindrome(s[i:j]):
                        # print('palindrome found:', s[i:j])
                        cur_pal = s[i:j]
                        if len(cur_pal) > longest_pal_length:
                            longest_pal = s[i:j]
                            longest_pal_length = j-i
                            # print('longest pal len:', longest_pal_length)
                            # print('new longest pal:', s[i:j])
                        j += 1
                i += 1

            return longest_pal
            """


sol = Solution()

inp = "babad"
print(sol.longestPalindrome(inp) == "bab")

inp = "cbbd"
print(sol.longestPalindrome(inp) == "bb")

inp = "bb"
print(sol.longestPalindrome(inp) == "bb")
