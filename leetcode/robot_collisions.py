# 2751. Robot Collisions
# https://leetcode.com/problems/robot-collisions/


# Based on editorial's Approach: Sorting & Stack
class Solution:
    def survivedRobotsHealths(
        self, positions: list[int], healths: list[int], directions: str
    ) -> list[int]:
        n = len(positions)
        indices = sorted(range(n), key=lambda i: positions[i])
        stack: list[int] = []  # Right-moving robots awaiting collision

        for cur in indices:
            if directions[cur] == "R":
                stack.append(cur)
                continue

            # Left-moving robot collides with right-moving ones on stack.
            while stack and healths[cur] > 0:
                top = stack[-1]
                if healths[top] > healths[cur]:
                    healths[top] -= 1
                    healths[cur] = 0
                elif healths[top] < healths[cur]:
                    healths[cur] -= 1
                    healths[top] = 0
                    stack.pop()
                else:
                    healths[top] = 0
                    healths[cur] = 0
                    stack.pop()

        return [healths[i] for i in range(n) if healths[i] > 0]
