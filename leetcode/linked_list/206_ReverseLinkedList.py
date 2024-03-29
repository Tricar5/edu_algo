"""
URL: https://leetcode.com/problems/reverse-linked-list/description/

Идея:

1) Идем двумя указателями по head
2) Указатель на предыдущий смотрит на None, curr на head
3) Указатели перемещаются вправо
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def displaylist(ll):
    ser = []

    while ll:
        ser.append(ll.val)
        ll = ll.next

    print(ser)


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            displaylist(prev)

        return prev


head = ListNode(1,
                ListNode(
                    2,
                    ListNode(
                        3,
                        ListNode(
                            4
                        )
                    )
                ))

c = Solution()

head = c.reverseList(head)

displaylist(head)
