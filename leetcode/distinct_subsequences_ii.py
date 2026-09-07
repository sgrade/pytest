# 940. Distinct Subsequences II
# https://leetcode.com/problems/distinct-subsequences-ii/


# Based on Editorial's Approach 1: Dynamic Programming
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        # dp[i] is the number of distinct subsequences of s[:i],
        # including the empty subsequence.
        dp = [1]
        last_index = {}
        for i, char in enumerate(s):
            # Each existing subsequence can stay as-is or append char.
            dp.append(dp[-1] * 2)
            # Repeats of char would double-count subsequences ending
            # at the previous occurrence of the same character.
            if char in last_index:
                dp[-1] -= dp[last_index[char]]
            last_index[char] = i

        # Exclude the empty subsequence.
        return (dp[-1] - 1) % (10**9 + 7)
