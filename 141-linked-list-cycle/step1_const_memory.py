# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode | None) -> bool:
        # 空の連結リスト、または単ノードからなる連結リストは明らかにサイクルを持たない
        if head is None or head.next is None:
            return False

        fast_pointer = head
        slow_pointer = head

        while True:
            fast_pointer = self._get_nexnex_node(fast_pointer)
            slow_pointer = slow_pointer.next

            if fast_pointer is None:
                return False
            if fast_pointer is slow_pointer:
                return True

    def _get_nexnex_node(self, node: ListNode) -> ListNode | None:
        next_node = node.next
        if next_node is None:
            return None
        return next_node.next
