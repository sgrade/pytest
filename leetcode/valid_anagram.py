# https://leetcode.com/problems/valid-anagram/description/

"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""


class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        # Too slow: "Your runtime beats 3.43 % of python3 submissions."
        s_list = list(s)
        for char in t:
            try:
                s_list.remove(char)
            except ValueError:
                return False
        if not s_list:
            return True
        else:
            return False


sol = Solution()
print(sol.isAnagram('anagram', 'nagaram'))  # True
print(sol.isAnagram('rat', 'car'))          # False
print(sol.isAnagram('ab', 'a'))             # False
print(sol.isAnagram('a', 'ab'))             # False
