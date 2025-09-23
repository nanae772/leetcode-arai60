# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode | None) -> ListNode | None:
        # setを使った純粋な回答
        visited = set()
        node = head

        while node is not None:
            if node in visited:
                return node
            visited.add(node)
            node = node.next

        return None
