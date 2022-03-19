"""
Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values.
(i.e., from left to right, level by level from leaf to root).
"""

# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrderBottom(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []

    nodes = []
    queue = [root]
    res = []

    while queue:
        temp_q = queue[:]
        queue.clear()
        level = []
        for node in temp_q:
            level.append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        nodes.append(level)

    for node in nodes[::-1]:
        res.append([x.val for x in node])

    return res
