# 2095. Delete the Middle Node of a Linked List
# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: ListNode | None) -> ListNode | None:
        # Empty list or single node — nothing to delete.
        if head is None or head.next is None:
            return None

        # slow stops at the node just before the middle; fast advances
        # at 2x speed so when fast is exhausted, slow is in position.
        slow: ListNode = head
        fast: ListNode | None = head.next.next
        while fast and fast.next:
            assert slow.next is not None  # invariant: slow trails fast by 2
            slow = slow.next
            fast = fast.next.next

        # Unlink the middle node.
        mid = slow.next
        assert mid is not None
        slow.next = mid.next
        return head
