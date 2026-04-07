# 2069. Walking Robot Simulation II
# https://leetcode.com/problems/walking-robot-simulation-ii/

# Based on Editorial's Walking Robot Simulation II
class Robot:
    _DIRS = ["East", "North", "West", "South"]

    def __init__(self, width: int, height: int):
        self._moved = False
        self._idx = 0

        # Pre-build every perimeter cell with its facing direction.
        # Traversal order: bottom (E) → right (N) → top (W) → left (S).
        p = []
        for x in range(width):
            p.append((x, 0, 0))
        for y in range(1, height):
            p.append((width - 1, y, 1))
        for x in range(width - 2, -1, -1):
            p.append((x, height - 1, 2))
        for y in range(height - 2, 0, -1):
            p.append((0, y, 3))

        # After a full lap, (0,0) is re-entered facing South, not East.
        p[0] = (0, 0, 3)
        self._perimeter = p

    def step(self, num: int) -> None:
        self._moved = True
        self._idx = (self._idx + num) % len(self._perimeter)

    def getPos(self) -> list[int]:
        x, y, _ = self._perimeter[self._idx]
        return [x, y]

    def getDir(self) -> str:
        # Before any step the robot faces East (initial direction).
        if not self._moved:
            return "East"
        _, _, d = self._perimeter[self._idx]
        return Robot._DIRS[d]


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()
