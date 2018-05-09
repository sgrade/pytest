# https://leetcode.com/problems/reverse-linked-list/description/

"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # https://leetcode.com/problems/reverse-linked-list/solution/

        previous = None
        current = head

        while current:
            next_temp = current.next
            current.next = previous
            previous = current
            current = next_temp

        return previous


ln1 = ListNode(1)
ln2 = ListNode(2)
ln3 = ListNode(3)
ln4 = ListNode(4)
ln5 = ListNode(5)
ln1.next = ln2
ln2.next = ln3
ln3.next = ln4
ln4.next = ln5

sol = Solution()
new_head = sol.reverseList(ln1)
print(type(new_head))
print(new_head.val)
print(new_head.next.val)
print(new_head.next.next.val)
print(new_head.next.next.next.val)
print(new_head.next.next.next.next.val)
print(new_head.next.next.next.next.next.val)
