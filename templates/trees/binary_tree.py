from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder(root):
    """Left -> Root -> Right. Returns sorted order for BST."""
    ans = []
    def dfs(node):
        if not node:
            return
        dfs(node.left)
        ans.append(node.val)
        dfs(node.right)
    dfs(root)
    return ans


def preorder(root):
    """Root -> Left -> Right."""
    ans = []
    def dfs(node):
        if not node:
            return
        ans.append(node.val)
        dfs(node.left)
        dfs(node.right)
    dfs(root)
    return ans


def postorder(root):
    """Left -> Right -> Root."""
    ans = []
    def dfs(node):
        if not node:
            return
        dfs(node.left)
        dfs(node.right)
        ans.append(node.val)
    dfs(root)
    return ans


def level_order(root):
    """BFS level-by-level traversal."""
    if not root:
        return []
    ans = []
    queue = deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        ans.append(level)
    return ans


def max_depth(root):
    """Height of tree."""
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


def invert_tree(root):
    """Mirror/invert binary tree."""
    if not root:
        return None
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root

