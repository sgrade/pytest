# 459. Repeated Substring Pattern
# https://leetcode.com/problems/repeated-substring-pattern/

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        i = 0
        subs = ""
        while (i + 1) * 2 <= n:
            subs += s[i]
            i += 1
            if n % i != 0:
                continue
            cnt = n // i
            if subs * cnt == s:
                return True
        return False
