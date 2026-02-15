# 67. Add Binary
# https://leetcode.com/problems/add-binary/


# Based on Editorial's Approach 2: Bit Manipulation
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num1, num2 = int(a, 2), int(b, 2)
        while num2:
            without_carry = num1 ^ num2
            carry = (num1 & num2) << 1
            num1, num2 = without_carry, carry
        return bin(num1)[2:]
