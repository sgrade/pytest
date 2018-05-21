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

        # https://leetcode.com/problems/valid-anagram/solution/

        # Approach  # 1 (Sorting) [Accepted]
        # 76 ms: "Your runtime beats 52.83 % of python3 submissions."
        """
        if len(s) != len(t):
            return False

        return sorted(list(s)) == sorted(list(t))
        """

        # Approach  # 2 (Hash Table) [Accepted]
        # 52 ms: "Your runtime beats 86.84 % of python3 submissions."
        if len(s) != len(t):
            return False

        hash_list = dict()
        
        for char in s:
            try:
                hash_list[char] += 1
            except KeyError:
                hash_list[char] = 1

        for char in t:
            try:
                hash_list[char] -= 1
            except KeyError:
                return False
            if hash_list[char] < 0:
                return False
        return True

        # My own
        # Too slow: "Your runtime beats 3.43 % of python3 submissions."
        """
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
        """


sol = Solution()
print(sol.isAnagram('anagram', 'nagaram'))  # True
print(sol.isAnagram('rat', 'car'))          # False
print(sol.isAnagram('ab', 'a'))             # False
print(sol.isAnagram('a', 'ab'))             # False
