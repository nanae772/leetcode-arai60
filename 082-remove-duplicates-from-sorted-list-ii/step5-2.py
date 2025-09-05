# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        # dummy を使わない実装
        head_without_duplicates = None
        node_without_duplicates = None
        node = head

        while node:
            if not node.next or node.val != node.next.val:
                if not head_without_duplicates:
                    head_without_duplicates = node
                else:
                    node_without_duplicates.next = node
                node_without_duplicates = node
                node = node.next
                node_without_duplicates.next = None
                continue

            duplicated_val = node.val
            while node and node.val == duplicated_val:
                node = node.next

        return head_without_duplicates
