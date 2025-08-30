# PRレビュー後の復習

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode | None) -> bool:
        """連結リストにサイクルがあるか判定する

        Args:
            head: 連結リストの先頭ノード

        Returns:
            bool: 連結リストにサイクルがあればTrue, そうでなければFalse
        """
        # Floyd's cycle-finding algorithmによる実装
        if head is None or head.next is None:
            return False

        fast_pointer = head
        slow_pointer = head

        while fast_pointer is not None and fast_pointer.next is not None:
            assert slow_pointer is not None, "slow_pointer should never be None here"
            fast_pointer = fast_pointer.next.next
            slow_pointer = slow_pointer.next

            if fast_pointer is slow_pointer:
                return True

        # fast_pointerが連結リストの末尾に到達できるならサイクルは無い
        return False
