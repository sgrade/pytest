# 2839. Check if Strings Can be Made Equal With Operations I
# https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-i/


class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        # Swaps only happen at distance 2, so even and odd positions
        # are independent groups. Both groups must have the same chars.
        return (sorted(s1[::2]) == sorted(s2[::2])
                and sorted(s1[1::2]) == sorted(s2[1::2]))
