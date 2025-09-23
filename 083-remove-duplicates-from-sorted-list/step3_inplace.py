# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        """与えられたソート済み連結リストの重複を削除する(in-place)

        Args:
            head: ソート済み連結リストの先頭

        Returns:
            ListNode | None: 重複を削除したソート済み連結リスト
        """
        node = head
        while node is not None:
            # 次のノードの値が今のノードの値と異なるかNoneになるまで、nextを繋ぎ変える
            while node.next is not None and node.next.val == node.val:
                node.next = node.next.next
            node = node.next
        return head
