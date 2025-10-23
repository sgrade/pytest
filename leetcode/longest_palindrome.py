# 409. Longest Palindrome
# https://leetcode.com/problems/longest-palindrome/

from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        ans = 0
        for cnt in counter.values():
            if cnt % 2 == 0:
                ans += cnt
            else:
                ans += cnt - 1
        if len(s) > ans:
            ans += 1
        return ans
