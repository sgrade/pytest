# 392. Is Subsequence
# https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_len = len(s)
        t_len = len(t)
        s_idx = 0
        t_idx = 0
        while s_idx < s_len:
            while t_idx < t_len and t[t_idx] != s[s_idx]:
                t_idx += 1
            if t_idx == t_len:
                return False
            s_idx += 1
            t_idx += 1
        return True if s_idx == s_len else False