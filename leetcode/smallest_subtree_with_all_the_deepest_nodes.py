# 865. Smallest Subtree with all the Deepest Nodes
# https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/

from collections import namedtuple
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Based on Editorial's Approach 2: Recursion
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        deepest = namedtuple("deepest", ("depth", "node"))

        def get_deepest(node: Optional[TreeNode]) -> deepest:
            if node is None:
                return deepest(0, None)
            left = get_deepest(node.left)
            right = get_deepest(node.right)
            if left.depth > right.depth:
                return deepest(left.depth + 1, left.node)
            if right.depth > left.depth:
                return deepest(right.depth + 1, right.node)
            return deepest(left.depth + 1, node)

        return get_deepest(root).node
