# 712. Minimum ASCII Delete Sum for Two Strings
# https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/


class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n1, n2 = len(s1), len(s2)

        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        for i in range(n1):
            dp[i + 1][0] = dp[i][0] + ord(s1[i])
        for j in range(n2):
            dp[0][j + 1] = dp[0][j] + ord(s2[j])

        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(
                        dp[i - 1][j] + ord(s1[i - 1]), dp[i][j - 1] + ord(s2[j - 1])
                    )

        return dp[n1][n2]
