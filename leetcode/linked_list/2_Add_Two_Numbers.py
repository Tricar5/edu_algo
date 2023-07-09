
"""
URL: https://leetcode.com/problems/add-two-numbers/description/

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        head = ListNode(0, None)
        tail = head

        while l1 or l2:

            if l1:
                tail.val += l1.val
                l1 = l1.next
            if l2:
                tail.val += l2.val
                l2 = l2.next

            if l1 or l2 or tail.val > 9:
                tail.next = ListNode(0, None)

                tail.next.val = tail.val // 10
                tail.val = tail.val % 10

                tail = tail.next

        return head