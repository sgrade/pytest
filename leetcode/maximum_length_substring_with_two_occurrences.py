# 3090. Maximum Length Substring With Two Occurrences
# https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/


class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        cntr = [0] * 26
        ans = 0
        left = 0
        for right in range(len(s)):
            i = ord(s[right]) - 97
            cntr[i] += 1
            if cntr[i] < 3:
                ans = max(ans, right - left + 1)
                continue
            while left < right and cntr[i] > 2:
                j = ord(s[left]) - 97
                cntr[j] -= 1
                left += 1
        return ans
