# 203. Remove Linked List Elements
# https://leetcode.com/problems/remove-linked-list-elements/


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        new_head = ListNode()
        new_head.next = head
        prev = new_head
        while head:
            if head.val != val:
                prev = head
                head = head.next
                continue
            # else
            head = head.next
            prev.next = head
        return new_head.next
