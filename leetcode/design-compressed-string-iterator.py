# 604. Design Compressed String Iterator
# https://leetcode.com/problems/design-compressed-string-iterator/

# Optimized with ideas from Leetcode's Sample 30 ms submission
class StringIterator:

    def __init__(self, compressedString: str):
        self.s = compressedString
        self.idx = 0
        self.cnt = 0
        self.next_idx = 0
        
    def next(self) -> str:
        if self.cnt > 0:
            self.cnt -= 1
            return self.s[self.idx]
        else:
            if self.next_idx == len(self.s):
                return ' '
            self.cnt = 0
            self.idx = self.next_idx
            self.next_idx += 1
            while self.next_idx < len(self.s) and self.s[self.next_idx].isdigit():
                self.cnt = self.cnt * 10 + int(self.s[self.next_idx])
                self.next_idx += 1
            self.cnt -= 1
            return self.s[self.idx]
        
    def hasNext(self) -> bool:
        return self.cnt > 0 or self.next_idx < len(self.s)

# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
