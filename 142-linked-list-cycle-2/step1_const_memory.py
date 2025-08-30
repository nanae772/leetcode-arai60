# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode | None) -> ListNode | None:
        if head is None or head.next is None:
            return None

        fast_pointer = head
        slow_pointer = head

        while fast_pointer is not None and fast_pointer.next is not None:
            fast_pointer = fast_pointer.next.next
            slow_pointer = slow_pointer.next

            if fast_pointer is slow_pointer:
                slow_pointer = head

                while fast_pointer is not slow_pointer:
                    fast_pointer = fast_pointer.next
                    slow_pointer = slow_pointer.next

                return fast_pointer

        return None
