# 2472. Maximum Number of Non-overlapping Palindrome Substrings
# https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings/


# Based on Editorial's Approach 2: Greedy
class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        def is_palindrome(left: int, right: int) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        count = 0
        next_start = 0
        n = len(s)

        # Take the leftmost palindrome of length k, else k + 1.
        for right in range(k - 1, n):
            for length in (k, k + 1):
                left = right - length + 1
                if left >= next_start and is_palindrome(left, right):
                    count += 1
                    next_start = right + 1
                    break

        return count
