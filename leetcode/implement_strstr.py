# https://leetcode.com/problems/implement-strstr/description/

"""
Implement strStr() - http://www.cplusplus.com/reference/cstring/strstr/.

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
"""


class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)


haystack = "hello"
needle = "ll"
x = Solution()
print(x.strStr(haystack, needle))