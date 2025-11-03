# 1578. Minimum Time to Make Rope Colorful
# https://leetcode.com/problems/minimum-time-to-make-rope-colorful/

from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = len(colors)
        if colors[n - 1] == "a":
            colors += "b"
        else:
            colors += "a"
        neededTime.append(0)
        total_time, cur_color_time, max_time_for_cur_color = (
            0,
            neededTime[0],
            neededTime[0],
        )
        for i in range(n):
            if colors[i] == colors[i + 1]:
                cur_color_time += neededTime[i + 1]
                max_time_for_cur_color = max(max_time_for_cur_color, neededTime[i + 1])
            else:
                total_time += cur_color_time - max_time_for_cur_color
                cur_color_time = neededTime[i + 1]
                max_time_for_cur_color = neededTime[i + 1]
        return total_time
