# 3498. Reverse Degree of a String
# https://leetcode.com/problems/reverse-degree-of-a-string/


class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0
        for i, ch in enumerate(s, 1):
            # Reversed alphabet: 'a' = 26, 'b' = 25, ..., 'z' = 1.
            reverse_pos = 26 - (ord(ch) - ord("a"))
            ans += reverse_pos * i
        return ans
