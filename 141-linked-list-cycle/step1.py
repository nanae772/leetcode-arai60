# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode | None) -> bool:
        checked_nodes = set()
        cur_node = head

        while cur_node is not None:
            if cur_node in checked_nodes:
                # 一度見たノードにもう一度訪れたならサイクルがある
                return True

            checked_nodes.add(cur_node)
            cur_node = cur_node.next

        return False
