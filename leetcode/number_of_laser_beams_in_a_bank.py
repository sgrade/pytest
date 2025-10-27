# 2125. Number of Laser Beams in a Bank
# https://leetcode.com/problems/number-of-laser-beams-in-a-bank/

from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev, cur, ans = 0, 0, 0
        prev = bank[0].count("1")
        for i in range(1, len(bank)):
            cur = bank[i].count("1")
            if cur:
                ans += prev * cur
                prev = cur
        return ans
