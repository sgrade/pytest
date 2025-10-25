# 1716. Calculate Money in Leetcode Bank
# https://leetcode.com/problems/calculate-money-in-leetcode-bank/


class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n // 7
        first_week = 28
        diff_each_week = 7
        # Ariphmetic sum
        full_weeks = weeks * (2 * first_week + (weeks - 1) * diff_each_week) // 2
        
        last_monday = 1 + weeks
        last_week = 0
        for day in range(n % 7):
            last_week += last_monday + day
        
        return full_weeks + last_week
