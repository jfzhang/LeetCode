"""
Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be
set to NULL. Initially, all next pointers are set to NULL.
"""


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def connect(root: 'Node') -> 'Node':
    if not root:
        return None

    q = [root]

    while q:
        temp_q = q[:]
        q.clear()
        size = len(temp_q)
        for i in range(size):
            temp_q[i].next = temp_q[i + 1] if i < size - 1 else None
            if temp_q[i].left:
                q.append(temp_q[i].left)
            if temp_q[i].right:
                q.append(temp_q[i].right)

    return root
