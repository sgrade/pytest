# 2833. Furthest Point From Origin
# https://leetcode.com/problems/furthest-point-from-origin/


class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        left, right, any = 0, 0, 0
        for move in moves:
            if move == "L":
                left += 1
            elif move == "R":
                right += 1
            else:
                any += 1
        return abs(left - right) + any
