#

"""Binary search tree (BST) is a binary tree where the value of each node is larger or equal to
the values in all the nodes in that node's left subtree and is smaller than the values in all
the nodes in that node's right subtree.

Write a function that checks if a given binary search tree contains a given value.

For example, for the following tree:

n1 (Value: 1, Left: null, Right: null)
n2 (Value: 2, Left: n1, Right: n3)
n3 (Value: 3, Left: null, Right: null)
Call to contains(n2, 3) should return True since a tree with root at n2 contains number 3."""

import collections


class BinarySearchTree:
    Node = collections.namedtuple('Node', ['left', 'right', 'value'])

    @staticmethod
    def contains(root, value):
        # print(root)
        if root is not None:
            root_value = root.value
            root_left = root.left
            root_right = root.right
            if root_value == value:
                # Found
                return True
            elif root_value <= value:
                # print('looking for', value, 'in the right node: ', root.right)
                return BinarySearchTree.contains(root_right, value)
            else:
                # print('looking in the levg node: ', root.left)
                return BinarySearchTree.contains(root_left, value)
        else:
            return False


n1 = BinarySearchTree.Node(value=1, left=None, right=None)
n3 = BinarySearchTree.Node(value=3, left=None, right=None)
n2 = BinarySearchTree.Node(value=2, left=n1, right=n3)
print(BinarySearchTree.contains(n2, 3))


# My own test case based on
# https://ru.wikipedia.org/wiki/Двоичное_дерево_поиска
"""
n1 =  BinarySearchTree.Node(value=1, left=None, right=None)
n4 =  BinarySearchTree.Node(value=4, left=None, right=None)
n7 =  BinarySearchTree.Node(value=7, left=None, right=None)
n6 =  BinarySearchTree.Node(value=6, left=n4, right=n7)
n13 =  BinarySearchTree.Node(value=13, left=None, right=None)
n14 =  BinarySearchTree.Node(value=14, left=n13, right=None)
n3 =  BinarySearchTree.Node(value=3, left=n1, right=n6)
n10 =  BinarySearchTree.Node(value=10, left=None, right=n14)
n8 =  BinarySearchTree.Node(value=8, left=n3, right=n10)

print(BinarySearchTree.contains(n8, 2))
"""