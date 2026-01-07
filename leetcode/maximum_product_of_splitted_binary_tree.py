# 1339. Maximum Product of Splitted Binary Tree
# https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        sums = []

        def get_sum(node):
            if node is None:
                return 0
            cur = node.val + get_sum(node.left) + get_sum(node.right)
            sums.append(cur)
            return cur

        total = get_sum(root)
        max_product = 0
        for s in sums:
            max_product = max(max_product, s * (total - s))
        return max_product % (10**9 + 7)
