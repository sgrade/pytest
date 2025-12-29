# 1176. Diet Plan Performance
# https://leetcode.com/problems/diet-plan-performance/


class Solution:
    def dietPlanPerformance(
        self, calories: list[int], k: int, lower: int, upper: int
    ) -> int:
        if len(calories) < k:
            return 0

        window_sum = sum(calories[:k])
        points = 0
        if window_sum < lower:
            points -= 1
        elif window_sum > upper:
            points += 1

        for i in range(len(calories) - k):
            window_sum = window_sum - calories[i] + calories[i + k]
            if window_sum < lower:
                points -= 1
            elif window_sum > upper:
                points += 1

        return points
