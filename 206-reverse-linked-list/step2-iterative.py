# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        node = head
        previous = None
        while node is not None:
            next_ = node.next
            node.next = previous
            previous = node
            node = next_
        # nodeがNoneであるとき、previousは元の連結リストの末尾=逆順リストの先頭
        return previous
