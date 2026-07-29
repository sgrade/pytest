# 3518. Smallest Palindromic Rearrangement II
# https://leetcode.com/problems/smallest-palindromic-rearrangement-ii/

from collections import Counter


# Based on Editorial's Approach:
# Combinatorial Mathematics + Trial and Error Method
class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        # A palindrome is determined by its left half, so only the first
        # half of the characters has to be rearranged.
        half_length = len(s) // 2
        char_counts = Counter(s[:half_length])
        distinct_chars = sorted(char_counts)

        def capped_comb(n: int, r: int) -> int:
            # C(n, r), capped at k + 1 to keep the numbers small.
            ans = 1
            for i in range(1, min(r, n - r) + 1):
                ans = ans * (n - i + 1) // i
                if ans > k:
                    return k + 1
            return ans

        def count_arrangements(slots: int) -> int:
            # Number of distinct orderings of the remaining characters:
            # pick the positions of each character in turn.
            total = 1
            for char in distinct_chars:
                total *= capped_comb(slots, char_counts[char])
                if total > k:
                    return k + 1
                slots -= char_counts[char]
            return total

        if count_arrangements(half_length) < k:
            return ""

        # Fill the left half position by position, each time leaving
        # remaining_slots to fill afterwards. Try the characters in
        # ascending order and skip whole blocks of arrangements that come
        # before the k-th one, shrinking k accordingly.
        left_chars = []
        for remaining_slots in reversed(range(half_length)):
            for char in distinct_chars:
                if not char_counts[char]:
                    continue

                char_counts[char] -= 1
                arrangements = count_arrangements(remaining_slots)
                if k <= arrangements:
                    left_chars.append(char)
                    break

                k -= arrangements
                char_counts[char] += 1

        left_half = "".join(left_chars)
        middle = s[half_length] if len(s) % 2 else ""
        return left_half + middle + left_half[::-1]
