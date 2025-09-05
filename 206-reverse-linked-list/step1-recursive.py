# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


import sys

# 問題の制約よりデフォルト(1000)より多く再帰できるようにする
sys.setrecursionlimit(10**4)


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        def reverse_list(node: ListNode | None, previous: ListNode | None) -> None:
            if node.next is None:
                node.next = previous
                # リストの末尾を逆順リストの先頭として返す
                return node

            head_reverse = reverse_list(node.next, node)
            node.next = previous
            return head_reverse

        if head is None:
            return None
        return reverse_list(head, None)
