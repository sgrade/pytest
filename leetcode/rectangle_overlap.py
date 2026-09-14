# 836. Rectangle Overlap
# https://leetcode.com/problems/rectangle-overlap/


# Based on Editorial's Approach #2: Check Area
class Solution:
    def isRectangleOverlap(self, rec1: list[int], rec2: list[int]) -> bool:
        # The rectangles overlap only if their intersection has a positive
        # area, i.e. it is non-empty on both axes independently.
        return (
            min(rec1[2], rec2[2]) > max(rec1[0], rec2[0])  # width > 0
            and min(rec1[3], rec2[3]) > max(rec1[1], rec2[1])  # height > 0
        )
