# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        # nodeは「既に１つしかないことが確定したノード」を指している
        dummy = ListNode(-float("inf"), head)
        node = dummy

        while node and node.next and node.next.next:
            if node.next.val != node.next.next.val:
                # node.next.valは１つしかないことが確定したのでnodeを１つ進める
                node = node.next
                continue

            # nextとnext.nextの値が重複しているなら、その値のノードは全て飛ばす
            duplicated_val = node.next.val
            while node.next is not None and node.next.val == duplicated_val:
                node.next = node.next.next

        return dummy.next
