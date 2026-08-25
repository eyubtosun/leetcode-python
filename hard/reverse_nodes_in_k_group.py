"""Reverse nodes of a linked list in groups of k."""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        dummy = ListNode(0, head)
        group_previous = dummy

        while True:
            kth = group_previous

            for _ in range(k):
                kth = kth.next

                if kth is None:
                    return dummy.next

            group_next = kth.next
            previous = group_next
            current = group_previous.next

            while current != group_next:
                next_node = current.next
                current.next = previous
                previous = current
                current = next_node

            old_group_start = group_previous.next
            group_previous.next = kth
            group_previous = old_group_start


def print_list(head: ListNode | None) -> None:
    values = []

    while head:
        values.append(head.val)
        head = head.next

    print(values)


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print_list(Solution().reverseKGroup(head, 2))
