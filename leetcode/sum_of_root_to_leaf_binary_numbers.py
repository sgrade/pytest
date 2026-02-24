# 1022. Sum of Root To Leaf Binary Numbers
# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumRootToLeaf(self, root: TreeNode | None) -> int:
        ans = 0
        stack = [(root, 0)]
        while stack:
            node, num = stack.pop()
            if node is not None:
                num = (num << 1) | node.val
                if node.left is None and node.right is None:
                    ans += num
                else:
                    stack.append((node.right, num))
                    stack.append((node.left, num))
        return ans
