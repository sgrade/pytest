# 757. Set Intersection Size At Least Two
# https://leetcode.com/problems/set-intersection-size-at-least-two/

from typing import List


# Based on Editorial's Approach #1: Greedy
class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        # Sort by start ascending, then by end descending
        intervals.sort(key=lambda x: (x[0], -x[1]))
        # Track how many points still needed for each interval (initially 2)
        to_pick_from_interval = [2] * len(intervals)
        min_len = 0
        # Process intervals from end (largest start) to beginning
        while intervals:
            (current_start, current_end), t = (
                intervals.pop(),
                to_pick_from_interval.pop(),
            )
            # Pick t points from the start of this interval
            for point in range(current_start, current_start + t):
                # Check if this point satisfies any remaining intervals
                for i, (s, e) in enumerate(intervals):
                    if to_pick_from_interval[i] and point <= e:
                        to_pick_from_interval[i] -= 1
                min_len += 1
        return min_len
