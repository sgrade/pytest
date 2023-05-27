# 1065. Index Pairs of a String
# https://leetcode.com/problems/index-pairs-of-a-string/

class Solution:
    def indexPairs(self, text: str, words: list[str]) -> list[list[int]]:
        ans = []
        for w in words:
            idx = 0
            while True:
                idx = text.find(w, idx)
                if idx == -1:
                    break
                ans.append([idx, idx + len(w) - 1])
                idx += 1
        ans.sort()
        return ans
