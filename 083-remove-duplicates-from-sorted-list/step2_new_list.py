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

        node = ListNode(head.val, None)
        head_uniq_list = node
        node_original = head

        while True:
            while node_original is not None and node_original.val == node.val:
                node_original = node_original.next
            if node_original is None:
                break
            node.next = ListNode(node_original.val, None)
            node = node.next

        return head_uniq_list
