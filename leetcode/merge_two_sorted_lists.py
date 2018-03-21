# https://leetcode.com/problems/merge-two-sorted-lists/description/
# DECIDED TO DO IT LATER.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        pass


ln1_1 = ListNode(1)
ln1_2 = ListNode(2)
ln1_3 = ListNode(4)
ln1_1.next = ln1_2
ln1_2.next = ln1_3
# print(ln1_1.next.next.val)

ln2_1 = ListNode(1)
ln2_2 = ListNode(3)
ln2_3 = ListNode(4)
ln2_1.next = ln2_2
ln2_2.next = ln2_3
# print(ln2_1.next.next.val)
