"""
Given the head of a singly linked list where elements are sorted in ascending order,
convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of
every node never differ by more than 1.
"""

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# inorder traversal of a binary tree will get all elements in ascending order
# use it assign back the value from list to tree
def sortedListToBST(head: Optional[ListNode]) -> Optional[TreeNode]:
    length = 0
    node = head
    while node:
        node = node.next
        length += 1

    if length == 0:
        return None

    def buildTree(left, right) -> TreeNode:
        nonlocal head
        if left > right:
            return None

        mid = (left + right) // 2
        root = TreeNode()
        root.left = buildTree(left, mid - 1)
        root.val = head.val
        head = head.next
        root.right = buildTree(mid + 1, right)

        return root

    return buildTree(0, length - 1)
