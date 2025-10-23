# 146. LRU Cache
# https://leetcode.com/problems/lru-cache/

# Some ideas are from Editorial's Approach 2: Hashmap + DoubleLinkedList
class ListNode():
    def __init__(self):
        self.key = 0
        self.value = 0
        self.prev: ListNode
        self.next: ListNode

class DLList():
    def __init__(self):
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def emplace_front(self, node):
        node.prev = self.head
        node.next = self.head.next
        node.next.prev = node
        self.head.next = node

    def remove_node(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def pop_back(self):
        node = self.tail.prev
        if node is not self.head:
            self.remove_node(node)
        return node
    
    def pop_front(self):
        node = self.head.next
        if node is not self.tail:
            self.remove_node(node)
        return node

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.capacity_used = 0
        self.keys = {}
        self.cache = DLList()

    def get(self, key: int) -> int:
        node = self.keys.get(key, None)
        if not node:
            return -1
        self.cache.remove_node(node)
        self.cache.emplace_front(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        node = self.keys.get(key, None)
        if node:
            node.value = value
            self.cache.remove_node(node)
            node.value = value
            self.cache.emplace_front(node)
            return
        if self.capacity_used == self.capacity:
            node = self.cache.pop_back()
            self.keys.pop(node.key)
        else:
            self.capacity_used += 1
        node = ListNode()
        node.key = key
        node.value = value
        self.cache.emplace_front(node)
        self.keys[key] = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
