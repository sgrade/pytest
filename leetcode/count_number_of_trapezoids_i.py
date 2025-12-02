# 3623. Count Number of Trapezoids I
# https://leetcode.com/problems/count-number-of-trapezoids-i/

from collections import defaultdict


class Solution:
    def countTrapezoids(self, points: list[list[int]]) -> int:
        MOD = 10**9 + 7
        points_on_level = defaultdict(int)
        for point in points:
            points_on_level[point[1]] += 1
        ans, total_edges = 0, 0
        for _, cnt in points_on_level.items():
            edges_on_level = cnt * (cnt - 1) // 2
            ans += edges_on_level * total_edges
            total_edges += edges_on_level
        return ans % MOD
