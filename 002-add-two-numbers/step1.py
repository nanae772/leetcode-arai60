# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: ListNode | None, l2: ListNode | None
    ) -> ListNode | None:
        dummy = ListNode(-1, None)
        node = dummy
        carry_digit = 0

        while l1 or l2 or carry_digit:
            l1_digit = 0
            l2_digit = 0
            if l1:
                l1_digit = l1.val
                l1 = l1.next
            if l2:
                l2_digit = l2.val
                l2 = l2.next

            sum_digit = l1_digit + l2_digit + carry_digit
            carry_digit, node_digit = sum_digit // 10, sum_digit % 10
            node.next = ListNode(node_digit, None)
            node = node.next

        return dummy.next
