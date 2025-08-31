# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        if head is None:
            return None

        node = head
        head_uniq_list = None

        while node is not None:
            next_node = node
            while next_node is not None and next_node.val == node.val:
                next_node = next_node.next

            node.next = next_node
            if node.val == head.val:
                head_uniq_list = node

            node = next_node

        assert head_uniq_list is not None
        return head_uniq_list
