# 3453. Separate Squares I
# https://leetcode.com/problems/separate-squares-i/


# Based on Editorial's Approach 1: Binary Search
class Solution:
    def separateSquares(self, squares: list[list[int]]) -> float:
        max_y, total_area = 0, 0
        for _, y, side in squares:
            total_area += side * side
            max_y = max(max_y, y + side)

        def has_half_area_below(target_y: float) -> bool:
            area_below_target = 0
            for _, y, side in squares:
                if y < target_y:
                    area_below_target += side * min(target_y - y, side)
            return area_below_target >= total_area / 2

        lo, hi = 0, max_y
        precision = 1e-5
        while abs(hi - lo) > precision:
            mid = (hi + lo) / 2
            if has_half_area_below(mid):
                hi = mid
            else:
                lo = mid
        return hi
