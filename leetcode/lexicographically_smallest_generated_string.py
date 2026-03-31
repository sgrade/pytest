# 3474. Lexicographically Smallest Generated String
# https://leetcode.com/problems/lexicographically-smallest-generated-string/


# Based on Editorial's Greedy approach.
class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        s = ["a"] * (n + m - 1)
        fixed = [False] * (n + m - 1)

        # Stamp str2 at every 'T' position.
        for i, ch in enumerate(str1):
            if ch == "T":
                for j, c in enumerate(str2, i):
                    if fixed[j] and s[j] != c:
                        return ""
                    s[j], fixed[j] = c, True

        # For each 'F' position, ensure str2 does NOT fully match.
        for i, ch in enumerate(str1):
            if ch == "F":
                if any(s[i + j] != c for j, c in enumerate(str2)):
                    continue  # Already differs somewhere.
                # Change the rightmost non-fixed char to 'b' (stays lex-small).
                for j in range(i + m - 1, i - 1, -1):
                    if not fixed[j]:
                        s[j] = "b"
                        break
                else:
                    return ""

        return "".join(s)
