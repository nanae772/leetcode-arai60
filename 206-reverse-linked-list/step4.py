class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        if head is None or head.next is None:
            return head
        head_reversed = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return head_reversed
