# Double linked list

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
