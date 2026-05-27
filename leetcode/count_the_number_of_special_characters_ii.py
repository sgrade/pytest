# 3121. Count the Number of Special Characters II
# https://leetcode.com/problems/count-the-number-of-special-characters-ii/


class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        first_upper_idx: dict = {}
        last_lower_idx: dict = {}
        for i, ch in enumerate(word):
            if ch.isupper():
                ch = ch.lower()
                if ch not in first_upper_idx:
                    first_upper_idx[ch] = i
        for i, ch in enumerate(word):
            if ch.islower():
                last_lower_idx[ch] = i
        ans = 0
        for ch, upper_idx in first_upper_idx.items():
            if ch in last_lower_idx and last_lower_idx[ch] < upper_idx:
                ans += 1
        return ans
