"""
URL: https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

Идея:
1) Дамми ноуд для нашего head - 1 (ListNode(0, next=head))
2) Два указателя. Левый стартует с дамми, правый смещен на n
3) Ищем окончание LL с помощью правого и просто меняем привязку по left

"""

from typing import Optional

#Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, next=head)
        left = dummy
        right = head

        for i in range(n):
            right = right.next

        while right:
            left = left.next
            right = right.next

        #delete

        left.next = left.next.next
        # l l.next l.next.next
        # 1 -> 2 -> 3

        return dummy.next