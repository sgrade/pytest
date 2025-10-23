# 3707. Equal Score Substrings
# https://leetcode.com/problems/equal-score-substrings/description/


class Solution:
    def scoreBalance(self, s: str) -> bool:
        prefix_score = set()
        score = 0
        for ch in s:
            score += ord(ch) - 96
            prefix_score.add(score)
        if score % 2 != 0:
            return False
        half_score = score // 2
        return half_score in prefix_score
