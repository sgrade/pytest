# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees
of every node never differ by more than 1.


Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    @staticmethod
    def sorted_array_to_bst(nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        def inner_function(arr):

            # corner cases
            arr_length = len(arr)
            if arr_length == 0:
                return

            mid = int(arr_length / 2)
            # print('mid', mid)
            root = TreeNode(arr[mid])
            # print('root', root.val)
            try:
                # print('\ntrying LEFT with array:', arr[:mid])
                root.left = inner_function(arr[:mid])
            except:
                return
            try:
                # print('\ntrying RIGHT with array:', arr[mid+1:])
                root.right = inner_function(arr[mid+1:])
            except:
                return


            return root

        return inner_function(nums)

# ++++++++++++++
# Helper function

# Utility function to print BST traversal
def bst_traversal_print(node):
    if not node:
        return
    print(node.val)
    bst_traversal_print(node.left)
    bst_traversal_print(node.right)


sol = Solution()
# inp = [1, 2, 3, 4, 5]
inp = [-10, -3, 0, 5, 9]
x = sol.sorted_array_to_bst(inp)
bst_traversal_print(x)
