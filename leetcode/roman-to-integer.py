# 13. Roman to Integer
# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        current, prev, ans = 0, 0, 0
        for ch in reversed(s):
            match ch:
                case 'M': current = 1000
                case 'D': current = 500
                case 'C': current = 100
                case 'L': current = 50
                case 'X': current = 10
                case 'V': current = 5
                case 'I': current = 1
            if current < prev: ans -= current
            else: ans += current
            prev = current
        return ans
