# 353. Design Snake Game
# https://leetcode.com/problems/design-snake-game/

from collections import deque


class SnakeGame:

    def __init__(self, width: int, height: int, food: list[list[int]]):
        self.score = 0
        self.cols = width
        self.rows = height
        self.food = deque(food)
        self.head_row = 0
        self.head_col = 0
        self.body = deque()
        self.body.append([0, 0])
        self.directions = {
            "U": [-1, 0],
            "D": [1, 0],
            "L": [0, -1],
            "R": [0, 1]
        }

    def move(self, direction: str) -> int:
        self.head_row += self.directions[direction][0]
        self.head_col += self.directions[direction][1]

        if self.head_row < 0 or self.head_row == self.rows or self.head_col < 0 or self.head_col == self.cols:
            return -1
        
        new_head = [self.head_row, self.head_col]

        if len(self.food) > 0 and self.head_row == self.food[0][0] and self.head_col == self.food[0][1]:
            self.score += 1
            self.food.popleft()
            self.body.appendleft(new_head)
            return self.score
        
        self.body.pop()
        if new_head in self.body:
            return -1
        self.body.appendleft(new_head)
        return self.score


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
