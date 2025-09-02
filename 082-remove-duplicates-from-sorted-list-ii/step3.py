# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


IMPOSSIBLE_VALUE = -1000  # 問題の制約上、ノードがとり得ない値にしておく


class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        dummy_node = ListNode(IMPOSSIBLE_VALUE, head)
        last_kept_node = dummy_node
        node = head

        while node is not None:
            while node.next is not None and node.next.val == node.val:
                node = node.next
            if last_kept_node.next is node:
                last_kept_node = node
            else:
                last_kept_node.next = node.next
            node = node.next

        return dummy_node.next
