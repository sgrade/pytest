# 2409. Count Days Spent Together
# https://leetcode.com/problems/count-days-spent-together/

import itertools

DAYS_IN_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# Days elapsed before each month starts: [0, 31, 59, ...].
DAYS_BEFORE_MONTH = [0, *itertools.accumulate(DAYS_IN_MONTH)]


# Based on Editorial's Approach: Convert Dates to Days of the Year and Calculate
#  the Difference
class Solution:
    def countDaysTogether(
        self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str
    ) -> int:
        # Overlap is [latest arrival, earliest departure], inclusive.
        overlap_start = max(
            self._day_of_year(arriveAlice), self._day_of_year(arriveBob)
        )
        overlap_end = min(
            self._day_of_year(leaveAlice), self._day_of_year(leaveBob)
        )
        return max(0, overlap_end - overlap_start + 1)

    def _day_of_year(self, date: str) -> int:
        """Converts an "MM-DD" date to its day number within the year."""
        month, day = map(int, date.split("-"))
        return DAYS_BEFORE_MONTH[month - 1] + day
