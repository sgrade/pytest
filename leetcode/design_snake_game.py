# 353. Design Snake Game
# https://leetcode.com/problems/design-snake-game/

from collections import deque


# Optimized with ideas from Leetcode's Sample 209 ms submission
class SnakeGame:

    def __init__(self, width: int, height: int, food: list[list[int]]):
        self.score = 0
        self.cols = width
        self.rows = height
        self.food = food
        self.body = deque()
        self.body.append([0, 0])
        self.directions = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

    def move(self, direction: str) -> int:
        head_row = self.body[0][0] + self.directions[direction][0]
        head_col = self.body[0][1] + self.directions[direction][1]
        new_head = [head_row, head_col]

        if self.score < len(self.food) and new_head == self.food[self.score]:
            self.score += 1
        else:
            self.body.pop()

        if new_head in self.body or head_row < 0 or head_row == self.rows or head_col < 0 or head_col == self.cols:
            return -1
            
        self.body.appendleft(new_head)
        return self.score


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
