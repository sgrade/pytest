"""
https://leetcode.com/problems/roman-to-integer/description/
Given a roman numeral, convert it to an integer.
Input is guaranteed to be within the range from 1 to 3999.
"""


class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        s_as_list = list(s)

        output = 0

        s_len = len(s_as_list)
        i = 0
        while i < s_len:
            if i+1 < s_len:
                if roman[s_as_list[i]] < roman[s_as_list[i+1]]:
                    output += (roman[s_as_list[i+1]] - roman[s_as_list[i]])
                    i += 2
                else:
                    output += roman[s_as_list[i]]
                    i += 1
            else:
                output += roman[s_as_list[i]]
                i += 1

        return output


input_numerals = 'MMMCMXCIX'
x = Solution()
print(x.romanToInt(input_numerals))
