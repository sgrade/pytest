# 3464. Maximize the Distance Between Points on a Square
# https://leetcode.com/problems/maximize-the-distance-between-points-on-a-square/


# Based on Editorial's Approach: Binary Search
from bisect import bisect_left


class Solution:
    def maxDistance(
        self,
        side: int,
        points: list[list[int]],
        k: int,
    ) -> int:
        # Map each border point to its position along the perimeter.
        pos = []

        for x, y in points:
            if x == 0:
                pos.append(y)
            elif y == side:
                pos.append(side + x)
            elif x == side:
                pos.append(side * 3 - y)
            else:
                pos.append(side * 4 - x)

        pos.sort()
        n = len(pos)
        perimeter = side * 4
        # Duplicate positions to handle wrap-around on the perimeter.
        pos2 = pos + [p + perimeter for p in pos]

        def check(limit: int) -> bool:
            # Greedily pick k points starting from each position.
            for i, start in enumerate(pos):
                end = start + perimeter - limit
                cur = start
                cur_idx = i

                for _ in range(k - 1):
                    nxt_idx = bisect_left(pos2, cur + limit, cur_idx + 1, i + n)
                    if nxt_idx >= i + n or pos2[nxt_idx] > end:
                        break
                    cur = pos2[nxt_idx]
                    cur_idx = nxt_idx
                else:
                    return True
            return False

        lo, hi = 0, perimeter
        ans = 0

        while lo <= hi:
            mid = (lo + hi) // 2
            if check(mid):
                lo = mid + 1
                ans = mid
            else:
                hi = mid - 1

        return ans
