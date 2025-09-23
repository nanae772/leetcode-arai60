# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        # 元のリストをin-placeで書き換えて重複を排除する
        node = head
        while node is not None:
            # 次のノードの値が今のノードの値と異なるかNoneになるまでnextを繋ぎ変える
            while node.next is not None and node.val == node.next.val:
                node.next = node.next.next
            node = node.next
        return head
