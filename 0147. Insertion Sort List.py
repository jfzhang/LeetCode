"""
Given the head of a singly linked list, sort the list using insertion sort, and return the sorted list's head.
"""


# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def insertionSortList(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head

    dummy_head = ListNode(0, head)
    pre = head
    curr = head.next

    while curr:
        if curr.val < pre.val:
            pre.next = curr.next

            node = dummy_head
            while curr.val > node.next.val:
                node = node.next
            curr.next = node.next
            node.next = curr
        else:
            pre = pre.next

        curr = pre.next

    return dummy_head.next
