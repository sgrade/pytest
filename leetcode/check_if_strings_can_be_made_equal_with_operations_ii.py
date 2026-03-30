# 2840. Check if Strings Can be Made Equal With Operations II
# https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-ii/


class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        return sorted(s1[::2]) == sorted(s2[::2]) and sorted(
            s1[1::2]
        ) == sorted(s2[1::2])
