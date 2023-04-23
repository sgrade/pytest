# 441. Arranging Coins
# https://leetcode.com/problems/arranging-coins/

from math import sqrt

# Math according to the Editorial
class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int(sqrt(2 * n + 0.25) - 0.5)
