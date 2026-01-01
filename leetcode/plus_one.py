# 66. Plus One
# https://leetcode.com/problems/plus-one/


class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        digits.reverse()
        carry = 1
        for i, digit in enumerate(digits):
            digit += carry
            if digit > 9:
                digit = 0
                carry = 1
            else:
                carry = 0
            digits[i] = digit
        if carry == 1:
            digits.append(1)
        digits.reverse()
        return digits
