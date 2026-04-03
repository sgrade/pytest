# 3661. Maximum Walls Destroyed by Robots
# https://leetcode.com/problems/maximum-walls-destroyed-by-robots/

from bisect import bisect_left, bisect_right


# Based on Editorial's Approach 3: Two Pointers + Dynamic Programming
#  + Space Optimization
class Solution:
    def maxWalls(
        self, robots: list[int], distance: list[int], walls: list[int]
    ) -> int:
        n = len(robots)
        bots = sorted(zip(robots, distance, strict=True))
        walls.sort()

        # sub_left / sub_right: best walls destroyed for robots 0..i
        # where robot i sweeps left / right.
        sub_left = sub_right = 0
        prev_right = 0

        for i, (pos, dist) in enumerate(bots):
            # Boundary indices around robot position
            # first wall strictly right of pos / first wall >= pos
            wall_at = bisect_right(walls, pos)
            wall_eq = bisect_left(walls, pos)

            # Left reach clipped to stay right of the previous robot
            left_bound = pos - dist
            if i > 0:
                left_bound = max(left_bound, bots[i - 1][0] + 1)
            current_left = wall_at - bisect_left(walls, left_bound)

            # Right reach clipped to stay left of the next robot
            right_bound = pos + dist
            if i < n - 1:
                right_bound = min(right_bound, bots[i + 1][0] - 1)
            current_right = bisect_right(walls, right_bound) - wall_eq

            if i == 0:
                sub_left = current_left
                sub_right = current_right
            else:
                # Walls in [prev_pos, pos]: the overlap zone for both robots
                between = wall_at - bisect_left(walls, bots[i - 1][0])
                overlap = min(current_left + prev_right, between)
                new_sub_left = max(
                    sub_left + current_left,
                    sub_right - prev_right + overlap,
                )
                sub_right = max(sub_left, sub_right) + current_right
                sub_left = new_sub_left

            prev_right = current_right

        return max(sub_left, sub_right)
