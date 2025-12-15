# 161. One Edit Distance
# https://leetcode.com/problems/one-edit-distance/


# Based on Editorial's Approach 1: One pass algorithm
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        len_s, len_t = len(s), len(t)
        if len_s < len_t:
            return self.isOneEditDistance(t, s)

        if len_s - len_t > 1:
            return False

        for i in range(len_t):
            if s[i] != t[i]:
                if len_s == len_t:
                    return s[i + 1 :] == t[i + 1 :]
                else:
                    return s[i + 1 :] == t[i:]

        return len_s == len_t + 1
