# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry = 0
        dummy = ListNode()
        current = dummy
        while l1 or l2 or carry:
            value1 = l1.val if l1 else 0
            value2 = l2.val if l2 else 0
            total = value1 + value2 + carry

            digit = total % 10
            current.next = ListNode(digit)
            current = current.next
            carry = total // 10

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next
