# https://leetcode.com/problems/linked-list-cycle/description/

"""
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        # https://leetcode.com/problems/linked-list-cycle/solution/

        # Approach #2 (Two Pointers)

        if not head or not head.next:
            return False

        slow = head
        fast = head.next
        while slow != fast:
            if not fast.next or not fast.next.next:
                return False
            slow = slow.next
            fast = fast.next.next

        return True


        # Approach #1 (Hash Table)
        # !!! Time Limit Exceeded !!!
        """
        nodes_seen = list()

        while head:
            if head in nodes_seen:
                return True
            else:
                nodes_seen.append(head)
            head = head.next

        return False
        """


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

ln1_1 = ListNode(1)
ln1_2 = ListNode(2)
ln1_3 = ListNode(4)
ln1_1.next = ln1_2
ln1_2.next = ln1_3
# the below line creates cycle
ln1_3.next = ln1_1

sol = Solution()
print(sol.hasCycle(ln1_1))