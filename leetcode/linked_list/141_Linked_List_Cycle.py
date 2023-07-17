"""

URL: https://leetcode.com/problems/linked-list-cycle/description/

Идея:

1) Два указателя
2) Один указатель движется на шаг, второй на два шага

"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None




class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        slow, fast = head, head

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                return True

        return False