# 3687. Library Late Fee Calculator
# https://leetcode.com/problems/library-late-fee-calculator/

from typing import List


class Solution:
    def lateFee(self, daysLate: List[int]) -> int:
        penalty = 0
        for days in daysLate:
            if days == 1:
                penalty += 1
            elif 2 <= days <= 5:
                penalty += 2 * days
            else:
                penalty += 3 * days
        return penalty
