# 489. Robot Room Cleaner
# https://leetcode.com/problems/robot-room-cleaner/


# Based on Editorial's Approach 1: Spiral Backtracking
# Clockwise directions: up, right, down, left.
_DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


class Solution:
    def cleanRoom(self, robot) -> None:
        visited: set[tuple[int, int]] = set()

        def go_back() -> None:
            """Reverse one step, restoring original orientation."""
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()

        def backtrack(row: int, col: int, d: int) -> None:
            visited.add((row, col))
            robot.clean()
            for i in range(4):
                nd = (d + i) % 4
                dr, dc = _DIRS[nd]
                nr, nc = row + dr, col + dc
                if (nr, nc) not in visited and robot.move():
                    backtrack(nr, nc, nd)
                    go_back()
                robot.turnRight()

        backtrack(0, 0, 0)
