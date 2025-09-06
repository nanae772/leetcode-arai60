# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        """連結リストを逆順にして返す(in-place)"""
        node = head
        previous = None
        while node is not None:
            next_ = node.next
            node.next = previous
            previous = node
            node = next_
        return previous
