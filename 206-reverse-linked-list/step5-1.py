class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        # 途中まで逆順にできているリストの頭を渡して、全て逆順にできたリストの頭を返してもらう方法
        def reverse_list_helper(
            head_rest: ListNode | None, head_reversed: ListNode | None
        ) -> ListNode | None:
            if head_rest is None:
                return head_reversed

            next_ = head_rest.next
            head_rest.next = head_reversed
            return reverse_list_helper(next_, head_rest)

        return reverse_list_helper(head, None)
