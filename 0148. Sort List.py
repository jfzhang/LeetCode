"""
Given the head of a linked list, return the list after sorting it in ascending order.
"""

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# divide and conquer
def sortList(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head

    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    head2 = slow.next
    slow.next = None
    part1 = sortList(head)
    part2 = sortList(head2)
    dummy = ListNode()
    node = dummy
    while part1 and part2:
        if part1.val < part2.val:
            node.next = part1
            part1 = part1.next
        else:
            node.next = part2
            part2 = part2.next
        node = node.next

    node.next = part1 if part1 else part2

    return dummy.next
