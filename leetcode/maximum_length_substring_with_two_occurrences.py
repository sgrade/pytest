# 3090. Maximum Length Substring With Two Occurrences
# https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/

from collections import Counter


class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        # Sliding window: shrink from the left whenever the new character
        # appears a third time, then record the window length.
        count = Counter()
        ans = 0
        left = 0
        for right, char in enumerate(s):
            count[char] += 1
            while count[char] > 2:
                count[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans
