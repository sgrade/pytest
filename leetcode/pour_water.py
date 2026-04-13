# 755. Pour Water
# https://leetcode.com/problems/pour-water/


# Based on Editorial's Approach 1: Simulation
# For each water unit, try moving left then right to find the lowest reachable
# position. If no lower position exists, water stays at K.
class Solution:
    def pourWater(
        self, heights: list[int], volume: int, k: int
    ) -> list[int]:
        for _ in range(volume):
            for d in (-1, 1):
                i = best = k
                while (
                    0 <= i + d < len(heights)
                    and heights[i + d] <= heights[i]
                ):
                    if heights[i + d] < heights[i]:
                        best = i + d
                    i += d
                if best != k:
                    heights[best] += 1
                    break
            else:
                heights[k] += 1
        return heights
