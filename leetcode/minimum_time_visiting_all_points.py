# 1266. Minimum Time Visiting All Points
# https://leetcode.com/problems/minimum-time-visiting-all-points/


class Solution:
    def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
        ans = 0
        for i in range(1, len(points)):
            x_diff = abs(points[i][0] - points[i - 1][0])
            y_diff = abs(points[i][1] - points[i - 1][1])
            ans += max(x_diff, y_diff)
        return ans
