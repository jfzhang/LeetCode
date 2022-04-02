"""
Given the root of a binary tree, return the postorder traversal of its nodes' values.
"""

# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def postorderTraversal(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return root

    res = []

    def postorder(node):
        if not node:
            return

        postorder(node.left)
        postorder(node.right)
        res.append(node.val)

    postorder(root)
    return res
