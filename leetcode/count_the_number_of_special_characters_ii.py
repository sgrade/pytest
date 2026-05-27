# 3121. Count the Number of Special Characters II
# https://leetcode.com/problems/count-the-number-of-special-characters-ii/


class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        # first index where the uppercase form appears
        first_upper: dict[str, int] = {}
        # last index where the lowercase form appears
        last_lower: dict[str, int] = {}
        for i, ch in enumerate(word):
            if ch.isupper():
                first_upper.setdefault(ch.lower(), i)
            else:
                last_lower[ch] = i

        # special: lowercase ends before uppercase begins
        return sum(
            last_lower.get(ch, first_upper[ch]) < idx
            for ch, idx in first_upper.items()
        )
