# 604. Design Compressed String Iterator
# https://leetcode.com/problems/design-compressed-string-iterator/

class StringIterator:

    def __init__(self, compressedString: str):
        self.s = ""
        i = 0
        while i < len(compressedString):
            j = i + 1
            while j < len(compressedString) and compressedString[j].isdigit():
                j += 1
            cnt = int(compressedString[i+1:j])
            self.s += compressedString[i] * cnt
            i = j
        self.idx = 0

    def next(self) -> str:
        has_next = self.hasNext()
        if not has_next:
            return ' '
        ch = self.s[self.idx]
        self.idx += 1
        return ch
        
    def hasNext(self) -> bool:
        return self.idx < len(self.s)

# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
