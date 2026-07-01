# 1358. Number of Substrings Containing All Three Characters
# https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/


# Based on Editorial's Approach 2: Last Position Tracking
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        last_idx = [-1] * 3
        ans = 0

        for cur_idx in range(len(s)):
            c = ord(s[cur_idx]) - 97
            last_idx[c] = cur_idx
            ans += 1 + min(last_idx)

        return ans
