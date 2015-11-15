#!/usr/bin/python3
# https://leetcode.com/problems/add-two-numbers/

class Solution(object):
    # Definition for singly-linked list.
    class ListNode(object):
        def __init__(self, *x):
            self.val = x[0] if x else None
            self.next = None

        def __iter__(self):
            current = self
            while current:
                yield current.val
                current = current.next

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = self.ListNode()
        q = 0
        current = result
        for a, b in zip(l1, l2):
            previous_q = q
            q, r = divmod(a + b, 10)
            current.next = self.ListNode(r + previous_q)
            current = current.next

        if q:
            current.next = self.ListNode(q)

        return result.next
