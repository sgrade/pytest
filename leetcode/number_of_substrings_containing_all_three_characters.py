# 1358. Number of Substrings Containing All Three Characters
# https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/


# Based on Editorial's Approach 2: Last Position Tracking
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        last_idx = [-1] * 3  # last seen index of 'a', 'b', 'c'
        ans = 0

        for cur_idx in range(len(s)):
            last_idx[ord(s[cur_idx]) - 97] = cur_idx
            # min(last_idx) is the latest index by which all three appear; every
            # left start in [0, min(last_idx)] yields a valid substring. If a
            # char is still missing, min is -1 and this adds 0.
            ans += 1 + min(last_idx)

        return ans
