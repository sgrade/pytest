# 2502. Design Memory Allocator
# https://leetcode.com/problems/design-memory-allocator/


class ListNode:
    def __init__(self, left: int, right: int, prev = None, next = None):
        self.left = left
        self.right = right
        self.prev = prev
        self.next = next

class DLList:
    def __init__(self, n: int):
        self.head = ListNode(0, 0)
        self.tail = ListNode(n, n)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def emplace(self, nxt_node, node):
        node.prev = nxt_node.prev
        nxt_node.prev.next = node
        node.next = nxt_node
        nxt_node.prev = node
    
    def erase(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

class Allocator:

    def __init__(self, n: int):
        self.n = n
        self.memory = DLList(n)
        self.blocks = {}

    def allocate(self, size: int, mID: int) -> int:
        left_it = self.memory.head
        right_it = self.memory.head.next
        while left_it and right_it:     # left_it here is only to avoid type checking errors
            left = left_it.right
            right = right_it.left
            if right - left >= size:
                new_block = ListNode(left, left + size)
                self.memory.emplace(right_it, new_block)
                if mID in self.blocks:
                    self.blocks[mID].append(new_block)
                else:
                    self.blocks[mID] = [new_block]
                return left
            left_it = left_it.next
            right_it = right_it.next
        return -1

    def free(self, mID: int) -> int:
        if mID not in self.blocks:
            return 0
        units = 0
        for block in self.blocks[mID]:
            units += block.right - block.left
            self.memory.erase(block)
        del self.blocks[mID]
        return units

# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.free(mID)
