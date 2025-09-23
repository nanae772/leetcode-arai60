# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        previous_unique_node = None
        head_of_new_list = None
        current_node = head

        while current_node is not None:
            if (
                current_node.next is not None
                and current_node.next.val == current_node.val
            ):
                start_val = current_node.val
                while current_node is not None and current_node.val == start_val:
                    current_node = current_node.next
            else:
                # １つしかない値なら、前に確定したノードをそのノードに繋げる
                # まだ先頭ノードが確定していなかったらそれを先頭ノードにする
                if previous_unique_node is None:
                    head_of_new_list = current_node
                else:
                    previous_unique_node.next = current_node
                previous_unique_node = current_node
                current_node = current_node.next

        if previous_unique_node is not None:
            previous_unique_node.next = None

        return head_of_new_list
