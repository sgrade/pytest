# 3517. Smallest Palindromic Rearrangement I
# https://leetcode.com/problems/smallest-palindromic-rearrangement-i/

from collections import defaultdict


class Solution:
    def smallestPalindrome(self, s: str) -> str:
        counter = defaultdict(int)
        for ch in s:
            counter[ch] += 1
        half = []
        mid = ''
        for ch, cnt in counter.items():
            if (cnt % 2 != 0):
                mid = ch
                half.extend(ch * ((cnt - 1) // 2))
            else:
                half.extend(ch * (cnt // 2))
        half.sort()
        ans = ''.join(half)
        ans += mid
        half.reverse()
        ans += ''.join(half)
        return ans
