# 434. Number of Segments in a String
# https://leetcode.com/problems/number-of-segments-in-a-string/

class Solution:
    def countSegments(self, s: str) -> int:
        ans = 0
        i = 0
        while i < len(s):
            while i < len(s) and s[i].isspace():
                i += 1
            if i < len(s) and not s[i].isspace():
                ans += 1
            while i < len(s) and not s[i].isspace():
                i += 1
        return ans

