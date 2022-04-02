"""
You are given the head of a singly linked-list. The list can be represented as:
L0 → L1 → … → Ln - 1 → Ln

Reorder the list to be on the following form:
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

You may not modify the values in the list's nodes. Only nodes themselves may be changed.
"""

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reorderList(head: Optional[ListNode]) -> None:
    """
    Do not return anything, modify head in-place instead.
    """
    if not head or not head.next or not head.next.next:
        return

    node = head
    node_list = []
    while node:
        node_list.append(node)
        node = node.next

    i, j = 0, len(node_list) - 1
    node = head
    while i < j:
        node_list[i].next = node_list[j]
        i += 1
        node_list[j].next = node_list[i]
        j -= 1
    node_list[i].next = None

    # if need O(1) space, do 1) find mid; 2) reverse 2nd half; 3) merge 1st half with the reversed 2nd half
