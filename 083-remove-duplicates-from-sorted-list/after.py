# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        """ソート済み連結リストから重複を削除する(in-place)"""
        if head is None:
            return None

        node = head
        while node.next is not None:
            if node.next.val == node.val:
                node.next = node.next.next
            else:
                node = node.next
        return head
