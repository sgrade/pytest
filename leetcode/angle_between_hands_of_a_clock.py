# 1344. Angle Between Hands of a Clock
# https://leetcode.com/problems/angle-between-hands-of-a-clock/


class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # minute hand: 6° per minute; hour hand: 30° per hour + 0.5° per minute
        minute_angle = 6 * minutes
        hour_angle = 30 * (hour % 12) + 0.5 * minutes
        diff = abs(hour_angle - minute_angle)
        return min(diff, 360 - diff)
