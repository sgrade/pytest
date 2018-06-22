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

        # Runtime: 128 ms
        # Your runtime beats 49.65 % of python3 submissions.

        def get_number(inp):
            output = ""
            while inp:
                output = str(inp.val) + output
                inp = inp.next
            return int(output)

        # Getting sum of two numbers
        # Then converting it to string, because string is easy to process
        # Then reversing it
        s = str(get_number(l1) + get_number(l2))[::-1]

        # An index for linked list creation
        i = len(s) - 1

        # Create linked list starting FROM THE LAST NODE TO THE FIRST
        # The very first statement required for cases where the list have only one element
        last = ListNode(int(s[i]))
        previous = last

        while i > 0:
            # Creating the node before previous (the one created before)
            current = ListNode(int(s[i-1]))
            # Link created node with the previous (the one created before)
            current.next = previous
            # Now last element is the one just created
            previous = current
            # Getting one step back to the list beginning
            i -= 1

        return previous


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