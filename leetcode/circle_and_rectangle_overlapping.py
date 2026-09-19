# 1401. Circle and Rectangle Overlapping
# https://leetcode.com/problems/circle-and-rectangle-overlapping/


# Based on Editorial's Approach 2: Minimum Distance from the Circle's Center to
# the Rectangle
class Solution:
    def checkOverlap(
        self,
        radius: int,
        xCenter: int,
        yCenter: int,
        x1: int,
        y1: int,
        x2: int,
        y2: int,
    ) -> bool:
        distance_squared = 0
        if xCenter < x1 or xCenter > x2:
            distance_squared += min((x1 - xCenter) ** 2, (x2 - xCenter) ** 2)
        if yCenter < y1 or yCenter > y2:
            distance_squared += min((y1 - yCenter) ** 2, (y2 - yCenter) ** 2)
        return distance_squared <= radius**2
