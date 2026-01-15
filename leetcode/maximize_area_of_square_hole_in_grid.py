# 2943. Maximize Area of Square Hole in Grid
# https://leetcode.com/problems/maximize-area-of-square-hole-in-grid/


class Solution:
    def maximizeSquareHoleArea(
        self, n: int, m: int, hBars: list[int], vBars: list[int]
    ) -> int:
        hBars.sort()
        vBars.sort()

        def get_longest_consequitive(bars: list[int]) -> int:
            longest = 1
            current = 1
            for i in range(1, len(bars)):
                if bars[i] == bars[i - 1] + 1:
                    current += 1
                else:
                    current = 1
                longest = max(longest, current)
            return longest

        h_max = get_longest_consequitive(hBars)
        v_max = get_longest_consequitive(vBars)

        side = min(h_max, v_max) + 1
        return side * side
