# https://leetcode.com/problems/add-two-numbers/description/



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        def rev_num(lst):
            rev_lst = lst[::-1]
            rev_num = int(''.join(str(x) for x in rev_lst))
            return rev_num

        l1_reversed = rev_num(l1)
        l2_reversed = rev_num(l2)

        sum_to_return = str(l1_reversed + l2_reversed)
        list_to_return = [int(i) for i in sum_to_return]
        list_to_return.reverse()

        return list_to_return


list1 = [2, 4, 3]
list2 = [5, 6, 4]



x = Solution()
print(x.addTwoNumbers(list1, list2))


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