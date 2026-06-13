# 3838. Weighted Word Mapping
# https://leetcode.com/problems/weighted-word-mapping/


from string import ascii_lowercase


class Solution:
    def mapWordWeights(self, words: list[str], weights: list[int]) -> str:
        # Reverse the alphabet so index i maps to the i-th letter from 'z'.
        letters = ascii_lowercase[::-1]
        # Sum each word's letter weights and pick the mapped letter (mod 26).
        return "".join(
            letters[sum(weights[ord(c) - 97] for c in word) % 26]
            for word in words
        )
