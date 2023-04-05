# 245. Shortest Word Distance III
# https://leetcode.com/problems/shortest-word-distance-iii/

class Solution:
    def shortestWordDistance(self, wordsDict: list[str], word1: str, word2: str) -> int:
        n = len(wordsDict)
        idx1 = n
        idx2 = -n
        ans = n
        if word1 == word2:
            for i in range(n):
                if wordsDict[i] == word1:
                    idx1 = i
                    if idx2 != -n:
                        ans = min(ans, idx1 - idx2)
                    idx2 = idx1
        else:
            for i in range(n):
                if wordsDict[i] == word1:
                    idx1 = i
                    if idx2 != -n:
                        ans = min(ans, idx1 - idx2)
                elif wordsDict[i] == word2:
                    idx2 = i
                    if idx1 != n:
                        ans = min(ans, idx2 - idx1)
        return ans
