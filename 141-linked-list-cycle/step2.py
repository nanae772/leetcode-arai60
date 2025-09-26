# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode | None) -> bool:
        if head is None or head.next is None:
            return False

        def get_node_two_ahead(node: ListNode) -> ListNode | None:
            if node.next is None:
                return None
            return node.next.next

        fast_pointer = head
        slow_pointer = head

        while True:
            fast_pointer = get_node_two_ahead(fast_pointer)
            slow_pointer = slow_pointer.next

            if fast_pointer is None:
                return False
            if fast_pointer is slow_pointer:
                return True
