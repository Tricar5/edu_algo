"""
URL: https://leetcode.com/problems/reorder-list/description/

Идеи:
1) Найти середину с помощью медленного и быстрого указания
2) Реверсировать вторую половину
4) Модифицировать наш LL попарно вставляя из первой и второй (реверсированной) половины
"""


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find middle
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half (Standard algo)

        second = slow.next
        prev = slow.next = None

        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt

        # merge two halfs
        first, second = head, prev

        while second:
            # Save next for each half
            tmp1, tmp2 = first.next, second.next
            # Insert pointers
            first.next = second
            second.next = tmp1
            # Shifting pointers
            first = tmp1
            second = tmp2