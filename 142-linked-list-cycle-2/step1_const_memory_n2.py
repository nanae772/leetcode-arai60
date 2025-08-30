# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode | None) -> ListNode | None:
        # Floyd's cycle detection を使用した解法
        # 注意：メモリはO(1)になっているが、時間がO(n^2)になってしまっている

        if head is None or head.next is None:
            return None

        fast_pointer = head
        slow_pointer = head

        while fast_pointer is not None and fast_pointer.next is not None:
            fast_pointer = fast_pointer.next.next
            slow_pointer = slow_pointer.next

            # サイクルが検出された場合
            if fast_pointer is slow_pointer:
                # まず、サイクルの長さを求める
                # 出会った地点からさらに出会うまでもう一週させる
                cycle_length = 0
                while True:
                    cycle_length += 1
                    fast_pointer = fast_pointer.next.next
                    slow_pointer = slow_pointer.next

                    if fast_pointer is slow_pointer:
                        break

                # サイクルの長さが求まった
                # 連結リストの先頭から順に、サイクルの長さ分だけ進めて元の位置に戻ってこれるかを判定する
                # 初めて戻ってこれたならそこがサイクルの始点である
                start_node = head

                while True:
                    current_node = start_node

                    for _ in range(cycle_length):
                        current_node = current_node.next

                    if current_node is start_node:
                        return start_node

                    start_node = start_node.next

        return None
