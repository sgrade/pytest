# https://leetcode.com/problems/delete-node-in-a-linked-list/description/

"""
Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

Supposed the linked list is 1 -> 2 -> 3 -> 4 and you are given the third node with value 3, the linked list should become 1 -> 2 -> 4 after calling your function.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        node.val = node.next.val
        node.next = node.next.next


sol = Solution()
ln1 = ListNode(1)
ln2 = ListNode(2)
ln3 = ListNode(3)
ln4 = ListNode(4)
ln5 = ListNode(5)
ln1.next = ln2
ln2.next = ln3
ln3.next = ln4
ln4.next = ln5

sol.deleteNode(ln3)
print(ln1.val)
print(ln1.next.val)
print(ln1.next.next.val)
print(ln1.next.next.next.val)