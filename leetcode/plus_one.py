# https://leetcode.com/problems/plus-one/description/

"""
Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.
"""


class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(len(digits) - 1, -1, -1):
            print(i)
            digit = digits[i] + 1
            if digit == 10:
                digits.insert(i, 0)
                digits.pop(i+1)
                if i == 0:
                    digits.insert(0, 1)
                    break
                continue
            else:
                digits.insert(i, digit)
                digits.pop(i + 1)
                break

        return digits


x = Solution()
inp = [9, 9, 9]
print(x.plusOne(inp))

