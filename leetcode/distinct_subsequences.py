# 115. Distinct Subsequences
# https://leetcode.com/problems/distinct-subsequences/


# Based on Editorial's Approach 2: Iterative Dynamic Programming
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        source_len, target_len = len(s), len(t)

        # counts[i][j] is the number of times t[j:] appears as a
        # subsequence of s[i:]. An empty target matches exactly once,
        # and an exhausted source matches nothing but an empty target.
        counts = [[0] * (target_len + 1) for _ in range(source_len + 1)]
        for i in range(source_len + 1):
            counts[i][target_len] = 1

        # Fill in reverse so both suffixes the cell depends on are known.
        for i in range(source_len - 1, -1, -1):
            for j in range(target_len - 1, -1, -1):
                # Skipping s[i] is always an option.
                counts[i][j] = counts[i + 1][j]

                # On a match, s[i] may also be consumed by t[j].
                if s[i] == t[j]:
                    counts[i][j] += counts[i + 1][j + 1]

        return counts[0][0]
