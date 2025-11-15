# 3234. Count the Number of Substrings With Dominant Ones
# https://leetcode.com/problems/count-the-number-of-substrings-with-dominant-ones/

# Based on Editorial's Approach: Enumeration
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        nearest_zero = [-1] * (n + 1)
        for i in range(n):
            if i == 0 or s[i - 1] == "0":
                nearest_zero[i + 1] = i
            else:
                nearest_zero[i + 1] = nearest_zero[i]

        ans = 0
        for i in range(1, n + 1):
            zeroes = 1 if s[i - 1] == "0" else 0
            j = i
            while j > 0 and zeroes * zeroes <= n:
                ones = (i - nearest_zero[j]) - zeroes
                if zeroes * zeroes <= ones:
                    ans += min(j - nearest_zero[j], ones - zeroes * zeroes + 1)
                j = nearest_zero[j]
                zeroes += 1
        return ans
