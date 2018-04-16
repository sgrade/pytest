# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        print('maxDepth function is issued')
        if root is None:
            return 0

        # Solution is from
        # http://jelices.blogspot.ru/2014/05/leetcode-python-maximum-depth-of-binary.html
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


# +++++++++++++++++++++++

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Tree1
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
sol = Solution()
print('Tree1 depth: ', sol.maxDepth(root))
