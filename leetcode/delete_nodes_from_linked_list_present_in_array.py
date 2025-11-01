# 3217. Delete Nodes From Linked List Present in Array
# https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def modifiedList(
        self, nums: List[int], head: Optional[ListNode]
    ) -> Optional[ListNode]:
        st = set(nums)
        prev = ListNode(next=head)
        pre_head = prev
        cur = head
        while cur:
            if cur.val in st:
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next
        return pre_head.next
