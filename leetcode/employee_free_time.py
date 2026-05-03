# 759. Employee Free Time
# https://leetcode.com/problems/employee-free-time/


# Definition for an Interval.
class Interval:  # noqa: B903
    def __init__(self, start: int = 0, end: int = 0):
        self.start = start
        self.end = end


# Based on Editorial's Approach: Events (Sort by Start)
class Solution:
    def employeeFreeTime(self, avails: list[list[Interval]]) -> list[Interval]:
        # Flatten all busy intervals sorted by start; a gap appears whenever
        # the next interval begins after the running max end seen so far.
        intervals = sorted(
            (iv for emp in avails for iv in emp), key=lambda iv: iv.start
        )
        ans = []
        end = intervals[0].end
        for iv in intervals[1:]:
            if iv.start > end:
                ans.append(Interval(end, iv.start))
            end = max(end, iv.end)
        return ans
