# 3863. Minimum Operations to Sort a String
# https://leetcode.com/problems/minimum-operations-to-sort-a-string/


class Solution:
    def minOperations(self, s: str) -> int:
        # Already sorted: nothing to do.
        if s == ''.join(sorted(s)):
            return 0

        # Length 2 and unsorted: sorting a proper substring can't help.
        if len(s) == 2:
            return -1

        min_char, max_char = min(s), max(s)

        # Sort a prefix/suffix that keeps the first min or last max in place.
        if s[0] == min_char or s[-1] == max_char:
            return 1

        # A min/max in the middle: sort a prefix, then a suffix (or vice
        # versa) to move it to its final end.
        middle = s[1:-1]
        if min_char in middle or max_char in middle:
            return 2

        # Min and max are only at the wrong ends: needs three operations.
        return 3
