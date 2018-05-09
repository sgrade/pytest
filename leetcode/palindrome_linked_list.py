# https://leetcode.com/problems/palindrome-linked-list/description/

"""
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        list_to_store_vals = list()

        while head:
            list_to_store_vals.append(head.val)
            head = head.next

        if list_to_store_vals == list_to_store_vals[::-1]:
            return True
        else:
            return False


sol = Solution()
ln1 = ListNode(1)
ln2 = ListNode(2)
ln3 = ListNode(2)
ln4 = ListNode(2)
ln5 = ListNode(1)
ln1.next = ln2
ln2.next = ln3
ln3.next = ln4
ln4.next = ln5

print(sol.isPalindrome(ln1))
