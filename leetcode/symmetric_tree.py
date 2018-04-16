# https://leetcode.com/problems/symmetric-tree/description/

"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        # Solution is from here:
        # https://www.geeksforgeeks.org/symmetric-tree-tree-which-is-mirror-image-of-itself/

        def is_mirror(root1, root2):
            if root1 is None and root2 is None:
                return True

            if root1 is not None and root2 is not None:
                if root1.val == root2.val:
                    return is_mirror(root1.left, root2.right) and is_mirror(root1.right, root2.left)

            return False

        return is_mirror(root, root)


# +++++++++++++++++++


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Symmetric
# tree1 = [1, 2, 2, 3, 4, 4, 3]
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)
sol = Solution()
print('Tree1: ', sol.isSymmetric(root))

# Not symmetric
# tree2 = [1, 2, 2, None, 3, None, 3]
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(None)
root.left.right = TreeNode(3)
root.right.left = TreeNode(None)
root.right.right = TreeNode(3)
sol = Solution()
print('Tree2: ', sol.isSymmetric(root))
