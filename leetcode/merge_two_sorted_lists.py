# https://leetcode.com/problems/merge-two-sorted-lists/description/

"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""

# Solution is from here - https://stackoverflow.com/a/40794749/9630183
# Explanation - https://www.youtube.com/watch?v=j_UNYW6Ap0k


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

        if l1 is None:
            return l2
        if l2 is None:
            return l1

        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l2.next, l1)
            return l2


ln1_1 = ListNode(1)
ln1_2 = ListNode(2)
ln1_3 = ListNode(4)
ln1_1.next = ln1_2
ln1_2.next = ln1_3
print('ln1_1: ', ln1_1)
print('ln1_2: ', ln1_2)
print('ln1_3: ', ln1_3)
# print(ln1_1.next.next.val)

ln2_1 = ListNode(1)
ln2_2 = ListNode(3)
ln2_3 = ListNode(4)
ln2_1.next = ln2_2
ln2_2.next = ln2_3
print('ln2_1: ', ln2_1)
print('ln2_2: ', ln2_2)
print('ln2_3: ', ln2_3)
# print(ln2_1.next.next.val)


x = Solution()
m_list = x.mergeTwoLists(ln1_1, ln2_1)
"""
print(m_list.val)
while m_list.next:
    print(m_list.next.val)
    m_list = m_list.next
"""