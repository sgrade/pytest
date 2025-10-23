# 1656. Design an Ordered Stream
# https://leetcode.com/problems/design-an-ordered-stream/

class OrderedStream:

    def __init__(self, n: int):
        self.chunks = [""] * (n + 1)
        self.idx = 1        

    def insert(self, idKey: int, value: str) -> list[str]:
        self.chunks[idKey] = value
        largest = []
        while self.idx < len(self.chunks):
            largest.append(self.chunks[self.idx])
            self.idx += 1
        return largest
