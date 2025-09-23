# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        # 元のリストを保ったまま、重複を削除した新しいリストを構築する
        if head is None:
            return None

        node_unique = ListNode(head.val, None)
        head_unique = node_unique
        node_original = head

        while True:
            while node_original is not None and node_original.val == node_unique.val:
                node_original = node_original.next
            if node_original is None:
                break
            node_unique.next = ListNode(node_original.val, None)
            node_unique = node_unique.next

        return head_unique
