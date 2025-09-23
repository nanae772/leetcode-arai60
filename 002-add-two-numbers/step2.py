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
        carry = 0

        while l1 or l2 or carry:
            l1_digit = 0
            l2_digit = 0
            if l1:
                l1_digit = l1.val
                l1 = l1.next
            if l2:
                l2_digit = l2.val
                l2 = l2.next

            sum_val = l1_digit + l2_digit + carry
            carry, new_val = sum_val // 10, sum_val % 10
            node.next = ListNode(new_val, None)
            node = node.next

        return dummy.next
