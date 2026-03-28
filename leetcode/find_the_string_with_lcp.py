# 2573. Find the String with LCP
# https://leetcode.com/problems/find-the-string-with-lcp/


# Based on Editorial's Approach: Greedy Construction
class Solution:
    def findTheString(self, lcp: list[list[int]]) -> str:
        n = len(lcp)
        word = [""] * n
        c = 0

        # Greedily assign the smallest available character.
        for i in range(n):
            if not word[i]:
                if c > 25:
                    return ""
                word[i] = chr(ord("a") + c)
                for j in range(i + 1, n):
                    if lcp[i][j]:
                        word[j] = word[i]
                c += 1

        # Rebuild LCP from word and compare against the input matrix.
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                expected = 0
                if word[i] == word[j]:
                    expected = (
                        1 if i == n - 1 or j == n - 1 else lcp[i + 1][j + 1] + 1
                    )
                if lcp[i][j] != expected:
                    return ""

        return "".join(word)
