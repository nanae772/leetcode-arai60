# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode | None) -> bool:
        visited = set()
        node = head

        while node is not None:
            if node in visited:
                # 一度見たノードにもう一度訪れたならサイクルがある
                return True

            visited.add(node)
            node = node.next

        return False
