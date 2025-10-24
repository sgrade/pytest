# 3517. Smallest Palindromic Rearrangement I
# https://leetcode.com/problems/smallest-palindromic-rearrangement-i/

from collections import Counter


class Solution:
    def smallestPalindrome(self, s: str) -> str:
        counter = Counter(s)
        half = []
        mid = ''
        
        # Process characters in sorted order
        for ch in sorted(counter.keys()):
            cnt = counter[ch]
            if cnt % 2 != 0:
                mid = ch
            half_cnt = cnt // 2
            half.append(ch * half_cnt)
        
        left = ''.join(half)
        return left + mid + left[::-1]
