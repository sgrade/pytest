# 2078. Two Furthest Houses With Different Colors
# https://leetcode.com/problems/two-furthest-houses-with-different-colors/


class Solution:
    def maxDistance(self, colors: list[int]) -> int:
        n = len(colors)
        # The furthest pair must include house 0 or house n-1.
        # Scan inward from each end to find the nearest different-color house.
        from_start = next(
            i for i in range(n - 1, -1, -1) if colors[i] != colors[0]
        )
        from_end = next(
            n - 1 - i for i in range(n) if colors[i] != colors[-1]
        )
        return max(from_start, from_end)
