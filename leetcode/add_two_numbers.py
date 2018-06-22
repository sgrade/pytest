# https://leetcode.com/problems/add-two-numbers/description/

"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        def get_number(inp):
            output = ""
            while inp:
                output = str(inp.val) + output
                inp = inp.next
            return int(output)

        def create_linked_list(first, nxt=()):
            lst = ListNode(first)
            lst_next = ListNode(nxt)
            lst.next = lst_next
            return lst_next

        def str_to_linked_list(s):
            if len(s) == 1:
                return ListNode(int(s[0]))
            else:
                return create_linked_list(s[0], str_to_linked_list(s[1:]))

        sum = get_number(l1) + get_number(l2)
        output_as_a_string = str(sum)[::-1]
        return str_to_linked_list(output_as_a_string)
        # TO DO: convert result to LinkedList


l11 = ListNode(2)
l12 = ListNode(4)
l13 = ListNode(3)
l11.next = l12
l12.next = l13

l21 = ListNode(5)
l22 = ListNode(6)
l23 = ListNode(4)
l21.next = l22
l22.next = l23

sol = Solution()
result = sol.addTwoNumbers(l11, l21)
print(result.val, result.next.val, result.next.next.val)


"""
# below is the solution, which works on leetcode. The above doesn't work as inputs are linked lists (not Python lists)
        def get_number(lst):
            number = str(lst.val)
            current = lst
            while current.next:
                val = current.next.val
                number = number + str(val)
                current = current.next
            return int(number)

        
        n1 = get_number(l1)
        n2 = get_number(l2)
        
        n = str(n1 + n2)
        n_list = [int(letter) for letter in n]
        n_list.reverse()
        
        return n_list
        
"""