"""Swap every two adjacent nodes in a singly linked list."""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(0, head)
        previous = dummy

        while previous.next and previous.next.next:
            first = previous.next
            second = first.next

            first.next = second.next
            second.next = first
            previous.next = second
            previous = first

        return dummy.next


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
result = Solution().swapPairs(head)

while result:
    print(result.val)
    result = result.next
