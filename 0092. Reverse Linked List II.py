"""
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of
the list from position left to position right, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Example 2:
Input: head = [5], left = 1, right = 1
Output: [5]

Constraints:
    The number of nodes in the list is n.
    1 <= n <= 500
    -500 <= Node.val <= 500
    1 <= left <= right <= n
"""
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseBetween(head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    if not head.next or left == right:
        return head

    # identify the "pre" node whose next is "left"
    dummy = ListNode(0, head)
    pre = dummy
    for _ in range(left - 1):
        pre = pre.next

    cur = pre.next
    # move cur.next before cur, and repeat this operation for (right - left) times
    for _ in range(right - left):
        nxt = cur.next
        cur.next = nxt.next
        nxt.next = pre.next
        pre.next = nxt

    return dummy.next


# Test Cases
# test cases
# [1,2,3,4,5] --> [1,4,3,2,5]
head = ListNode(1)
node1 = head
for i in [2, 3, 4, 5]:
    node2 = ListNode(i)
    node1.next = node2
    node1 = node2
reverseBetween(head, 2, 4)

node1 = ListNode(5)
head = ListNode(3, node1)
reverseBetween(head, 1, 2)
