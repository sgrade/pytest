# 1189. Maximum Number of Balloons
# https://leetcode.com/problems/maximum-number-of-balloons/

from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # Count letters in text and in the word "balloon".
        have = Counter(text)
        need = Counter("balloon")
        # Each balloon needs `cnt` copies of letter `c`; the limiting
        # letter determines how many full words we can build.
        return min(have[c] // cnt for c, cnt in need.items())
