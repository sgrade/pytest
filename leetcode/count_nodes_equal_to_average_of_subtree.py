# 2265. Count Nodes Equal to Average of Subtree
# https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        ans = 0

        def post_order(node: TreeNode) -> tuple[int, int]:
            # Return (subtree sum, subtree size) and count matches.
            nonlocal ans
            total_sum = node.val
            nodes = 1
            if node.left:
                child_sum, child_nodes = post_order(node.left)
                total_sum += child_sum
                nodes += child_nodes
            if node.right:
                child_sum, child_nodes = post_order(node.right)
                total_sum += child_sum
                nodes += child_nodes
            # Floor of the subtree average, matching the problem.
            if total_sum // nodes == node.val:
                ans += 1
            return total_sum, nodes

        post_order(root)
        return ans
