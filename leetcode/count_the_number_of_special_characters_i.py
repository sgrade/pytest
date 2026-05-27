# 3120. Count the Number of Special Characters I
# https://leetcode.com/problems/count-the-number-of-special-characters-i/


class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        chars = set(word)
        # A letter is "special" if both its lower and upper forms appear.
        return sum(
            c in chars and c.upper() in chars
            for c in "abcdefghijklmnopqrstuvwxyz"
        )
