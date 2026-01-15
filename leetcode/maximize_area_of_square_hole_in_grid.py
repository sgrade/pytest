# 2943. Maximize Area of Square Hole in Grid
# https://leetcode.com/problems/maximize-area-of-square-hole-in-grid/


class Solution:
    def maximizeSquareHoleArea(
        self, n: int, m: int, hBars: list[int], vBars: list[int]
    ) -> int:
        hBars.sort()
        vBars.sort()

        h_max, h_cur, v_max, v_cur = 1, 1, 1, 1
        for i in range(1, len(hBars)):
            if hBars[i] == hBars[i - 1] + 1:
                h_cur += 1
            else:
                h_cur = 1
            h_max = max(h_max, h_cur)
        for i in range(1, len(vBars)):
            if vBars[i] == vBars[i - 1] + 1:
                v_cur += 1
            else:
                v_cur = 1
            v_max = max(v_max, v_cur)

        side = min(h_max, v_max) + 1
        return side * side
