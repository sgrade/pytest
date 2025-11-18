# 717. 1-bit and 2-bit Characters
# https://leetcode.com/problems/1-bit-and-2-bit-characters/

from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        ones = 0
        for i in range(len(bits) - 2, -1, -1):
            if bits[i] == 1:
                ones += 1
            else:
                break
        return ones % 2 == 0
