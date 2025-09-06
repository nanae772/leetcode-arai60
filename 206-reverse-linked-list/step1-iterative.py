# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        if head is None:
            return None

        nodes = []
        node = head
        while node is not None:
            nodes.append(node)
            node = node.next

        head_reverse = nodes[-1]
        while nodes:
            node_reverse = nodes.pop()
            if not nodes:
                node_reverse.next = None
                break
            node_reverse.next = nodes[-1]

        return head_reverse
