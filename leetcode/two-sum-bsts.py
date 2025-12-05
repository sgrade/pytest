# 1214. Two Sum BSTs
# https://leetcode.com/problems/two-sum-bsts/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


# Based on Editorial's Approach 4: Two Pointers
class Solution:
    def twoSumBSTs(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int
    ) -> bool:
        def dfs(node, nodes):
            if not node:
                return
            dfs(node.left, nodes)
            nodes.append(node.val)
            dfs(node.right, nodes)

        (
            nodes1,
            nodes2,
        ) = [], []
        dfs(root1, nodes1)
        dfs(root2, nodes2)

        i1, i2 = 0, len(nodes2) - 1
        while i1 < len(nodes1) and i2 >= 0:
            if nodes1[i1] + nodes2[i2] == target:
                return True
            elif nodes1[i1] + nodes2[i2] < target:
                i1 += 1
            else:
                i2 -= 1
        return False
