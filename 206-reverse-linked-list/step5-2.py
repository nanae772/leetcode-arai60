class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        # 何も渡さずに自分より後の連結リストを逆順にしてもらって、その逆順リストの尾を自分に繋ぎかえる
        def reverse_list_helper(node: ListNode | None) -> ListNode | None:
            if node is None or node.next is None:
                return node

            head_reversed = reverse_list_helper(node.next)
            tail_reversed = node.next
            tail_reversed.next = node
            node.next = None
            return head_reversed

        return reverse_list_helper(head)
