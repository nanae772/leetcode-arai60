# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode | None) -> ListNode | None:
        """連結リストのサイクルの始点を返す（サイクルが無ければNoneを返す）

        Args:
            head: 連結リストの先頭

        Returns:
            ListNode | None: 連結リストに含まれるサイクルの始点（サイクルが無ければNone）
        """
        # Floyd's cycle-finding algorithmによる実装
        if head is None or head.next is None:
            return None

        fast_pointer = head
        slow_pointer = head
        has_cycle = False

        while fast_pointer is not None and fast_pointer.next is not None:
            fast_pointer = fast_pointer.next.next
            slow_pointer = slow_pointer.next

            if fast_pointer is slow_pointer:
                has_cycle = True
                break

        if has_cycle:
            # サイクルの始点を探す
            slow_pointer = head
            while fast_pointer is not slow_pointer:
                fast_pointer = fast_pointer.next
                slow_pointer = slow_pointer.next
            return fast_pointer
        else:
            return None
