# 835. Image Overlap
# https://leetcode.com/problems/image-overlap/


from collections import Counter


class Solution:
    def largestOverlap(
        self, img1: list[list[int]], img2: list[list[int]]
    ) -> int:
        # Only the cells with 1 can contribute to an overlap.
        ones1 = [
            (r, c)
            for r, row in enumerate(img1)
            for c, value in enumerate(row)
            if value
        ]
        ones2 = [
            (r, c)
            for r, row in enumerate(img2)
            for c, value in enumerate(row)
            if value
        ]

        # A pair of ones overlaps exactly when img1 is shifted by the vector
        # between them, so the most frequent vector gives the best overlap.
        shifts = Counter(
            (r2 - r1, c2 - c1) for r1, c1 in ones1 for r2, c2 in ones2
        )

        return max(shifts.values(), default=0)
