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
                return self._find_cycle_start(head, fast_pointer)

        return None

    def _find_cycle_start(
        self,
        head: ListNode,
        meeting_node: ListNode,
    ) -> ListNode:
        node_from_head = head
        node_from_meet = meeting_node

        while node_from_head is not node_from_meet:
            node_from_head = node_from_head.next
            node_from_meet = node_from_meet.next

        return node_from_head
