# 549. Binary Tree Longest Consecutive Sequence II
# https://leetcode.com/problems/binary-tree-longest-consecutive-sequence-ii/

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        def get_len(node: Optional[TreeNode]) -> list[int]:
            nonlocal max_len

            if not node:
                return [0, 0]

            incr_len, decr_len = 1, 1

            if node.left:
                left = get_len(node.left)
                if node.val == node.left.val - 1:
                    incr_len = left[0] + 1
                elif node.val == node.left.val + 1:
                    decr_len = left[1] + 1

            if node.right:
                right = get_len(node.right)
                if node.val == node.right.val - 1:
                    incr_len = max(incr_len, right[0] + 1)
                if node.val == node.right.val + 1:
                    decr_len = max(decr_len, right[1] + 1)

            max_len = max(max_len, incr_len + decr_len - 1)
            return [incr_len, decr_len]

        max_len = 0
        get_len(root)
        return max_len
