# 362. Design Hit Counter
# https://leetcode.com/problems/design-hit-counter/

from collections import deque

class HitCounter:

    def __init__(self):
        self.hits = deque()
        self.total = 0

    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp)
        self.total += 1

    def getHits(self, timestamp: int) -> int:
        while len(self.hits) > 0 and self.hits[0] < timestamp - 299:
            self.total -= 1
            self.hits.popleft()
        return self.total


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
