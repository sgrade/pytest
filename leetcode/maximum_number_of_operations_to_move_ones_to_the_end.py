# 3228. Maximum Number of Operations to Move Ones to the End
# https://leetcode.com/problems/maximum-number-of-operations-to-move-ones-to-the-end/


class Solution:
    def maxOperations(self, s: str) -> int:
        ops = 0
        zero_intervals = 0
        i = len(s) - 1
        while i >= 0:
            if s[i] == "0":
                zero_intervals += 1
                while i >= 0 and s[i] == "0":
                    i -= 1
            else:
                ones = 0
                while i >= 0 and s[i] == "1":
                    ones += 1
                    i -= 1
                ops += ones * zero_intervals
        return ops
