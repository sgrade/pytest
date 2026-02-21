# 1967. Number of Strings That Appear as Substrings in Word
# https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/


class Solution:
    def numOfStrings(self, patterns: list[str], word: str) -> int:
        substrings = 0
        for pattern in patterns:
            if pattern in word:
                substrings += 1
        return substrings
