class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head):
    """Reverse linked list iteratively."""
    prev = None
    while head:
        next_node = head.next
        head.next = prev
        prev = head
        head = next_node
    return prev


def find_middle(head):
    """Find middle node (second middle if even length)."""
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def has_cycle(head):
    """Detect if linked list has a cycle."""
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


def merge_two_sorted(l1, l2):
    """Merge two sorted linked lists."""
    dummy = ListNode()
    curr = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    curr.next = l1 or l2
    return dummy.next


def delete_node(head, val):
    """Delete first node with given value."""
    dummy = ListNode(next=head)
    prev = dummy
    while prev.next:
        if prev.next.val == val:
            prev.next = prev.next.next
            break
        prev = prev.next
    return dummy.next


def get_nth_from_end(head, n):
    """Get nth node from end (1-indexed)."""
    fast = slow = head
    for _ in range(n):
        fast = fast.next
    while fast:
        slow = slow.next
        fast = fast.next
    return slow

