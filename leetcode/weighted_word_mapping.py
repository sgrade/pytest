# 3838. Weighted Word Mapping
# https://leetcode.com/problems/weighted-word-mapping/


from string import ascii_lowercase


class Solution:
    def mapWordWeights(self, words: list[str], weights: list[int]) -> str:
        letters = "".join(reversed(ascii_lowercase))
        ans = ""
        for word in words:
            total = 0
            for ch in word:
                weight_idx = ord(ch) - 97
                total += weights[weight_idx]
            ans += letters[total % 26]
        return ans
