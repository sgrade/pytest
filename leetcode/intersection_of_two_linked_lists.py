# https://leetcode.com/problems/intersection-of-two-linked-lists/description/

"""
Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        # https://leetcode.com/problems/intersection-of-two-linked-lists/solution/
        # Approach #3 (Two Pointers)
        if headA and headB:

            p_a = headA
            a_len = 1
            while p_a.next:
                p_a = p_a.next
                a_len += 1
            p_a = headB

            p_b = headB
            b_len = 1
            while p_b.next:
                p_b = p_b.next
                b_len += 1
            p_b = headA

            len_diff = a_len - b_len

            i = 0
            if len_diff > 0:
                while i < len_diff:
                    p_b = p_b.next
                    i += 1
            elif len_diff < 0:
                while i < (-len_diff):
                    p_a = p_a.next
                    i += 1

            while p_a != p_b and p_a and p_b:
                p_a = p_a.next
                p_b = p_b.next
            else:
                return p_a

        return None


        """
        # Approach #2 (Hash Table)
        # Time Limit Exceeded
        # Last executed input: 
        # Intersected at '20000': [1,3,5,7,9...
        if headA and headB:

            _hash = list()

            a = headA
            while a:
                _hash.append(a)
                a = a.next

            b = headB
            while b:
                if b in _hash:
                    return b
                b = b.next

        return None
        """

        """
        # The below solution will just show if the lists are intersected or not
        # But according the the task it should return the node where they are intersected
        if headA and headB:

            a = headA
            while a.next:
                a = a.next

            b = headB
            while b.next:
                b = b.next

            if a is b:
                return a

        return None
        """


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


ln0_1 = ListNode(0)
ln1_1 = ListNode(11)
ln1_2 = ListNode(12)
# ln1_3 = ListNode(4)
ln0_1.next = ln1_1
ln1_1.next = ln1_2
# no intersection
# ln1_2.next = ln1_3

ln2_1 = ListNode(21)
ln2_2 = ListNode(22)
ln2_3 = ListNode(999)
ln2_1.next = ln2_2
ln2_2.next = ln2_3
# Intersection
ln1_2.next = ln2_3


"""
# Corner case - no intersection
ln1_1 = []
ln2_1 = []
"""

x = Solution()
result = x.getIntersectionNode(ln0_1, ln2_1)
if result:
    print(result.val)
else:
    print('None')
#print(x.getIntersectionNode(ln1_1, ln2_1).val)
