# https://leetcode.com/problems/excel-sheet-column-number/description/

"""
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701

Input: "AAA"
Output: 703

"""

import string


class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """

        # https://stackoverflow.com/questions/5927149/get-character-position-in-alphabet
        # https://www.geeksforgeeks.org/find-excel-column-number-column-title/

        i = 0
        output = 0
        for char in s[::-1]:
            position = string.ascii_lowercase.index(char.lower()) + 1
            output += position * 26**i
            print(output)
            i += 1
        return output


sol = Solution()
inp = "AAA"
print(sol.titleToNumber(inp))
