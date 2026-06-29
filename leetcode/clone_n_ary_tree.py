# 1490. Clone N-ary Tree
# https://leetcode.com/problems/clone-n-ary-tree/


# Definition for a Node.
class Node:
    def __init__(
        self, val: int | None = None, children: list["Node"] | None = None
    ):
        self.val = val
        self.children = children if children is not None else []


class Solution:
    def cloneTree(self, root: "Node") -> "Node":
        if not root:
            return root
        ans = Node(root.val)
        for child in root.children:
            ans.children.append(self.cloneTree(child))
        return ans
