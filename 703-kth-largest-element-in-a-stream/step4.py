from typing import Generic, TypeVar

T = TypeVar("T")


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.top_k_largest = MinHeap()
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        self.top_k_largest.push(val)
        if len(self.top_k_largest) > self.k:
            self.top_k_largest.pop()
        return self.top_k_largest.peek()


class MinHeap:
    """最小ヒープ"""

    def __init__(self, array: list[T] = []) -> None:
        self.heap = array[:]
        for i in reversed(range(len(self.heap))):
            self._heapify_subtree(i)

    def __len__(self) -> int:
        return len(self.heap)

    def peek(self) -> T:
        """最小値を返す"""
        if not self.heap:
            raise IndexError("heap is empty.")
        return self.heap[0]

    def push(self, value: T) -> None:
        """ヒープにvalueを挿入する"""
        self.heap.append(value)
        self._shift_up(len(self.heap) - 1)

    def pop(self) -> T:
        """ヒープから最小値を取り出し、その値を返す"""
        if not self.heap:
            raise IndexError("heap is empty.")

        top = self.heap[0]
        self._swap(0, len(self.heap) - 1)
        self.heap.pop()
        if self.heap:
            self._heapify_subtree(0)
        return top

    def _shift_up(self, i: int) -> None:
        assert 0 <= i < len(self.heap)
        parent_value = self._get_parent_value(i)
        if parent_value is None or parent_value <= self.heap[i]:
            return

        self._swap(i, self._get_parent_index(i))
        self._shift_up(self._get_parent_index(i))

    def _heapify_subtree(self, i: int) -> None:
        assert 0 <= i < len(self.heap)
        left_value = self._get_left_value(i)
        right_value = self._get_right_value(i)

        min_value = self.heap[i]
        if left_value is not None:
            min_value = min(min_value, left_value)
        if right_value is not None:
            min_value = min(min_value, right_value)

        if min_value == self.heap[i]:
            return

        if min_value == left_value:
            self._swap(i, self._get_left_index(i))
            self._heapify_subtree(self._get_left_index(i))
        else:
            self._swap(i, self._get_right_index(i))
            self._heapify_subtree(self._get_right_index(i))

    def _swap(self, i_0: int, i_1: int) -> None:
        assert 0 <= i_0 < len(self.heap)
        assert 0 <= i_1 < len(self.heap)
        self.heap[i_0], self.heap[i_1] = self.heap[i_1], self.heap[i_0]

    def _get_parent_index(self, i: int) -> None:
        return (i - 1) // 2

    def _get_left_index(self, i: int) -> int:
        return 2 * i + 1

    def _get_right_index(self, i: int) -> int:
        return 2 * i + 2

    def _get_parent_value(self, i: int) -> T | None:
        assert 0 <= i < len(self.heap)
        if i == 0:
            return None
        return self.heap[self._get_parent_index(i)]

    def _get_left_value(self, i: int) -> T | None:
        assert 0 <= i < len(self.heap)
        if self._get_left_index(i) >= len(self.heap):
            return None
        return self.heap[self._get_left_index(i)]

    def _get_right_value(self, i: int) -> T | None:
        assert 0 <= i < len(self.heap)
        if self._get_right_index(i) >= len(self.heap):
            return None
        return self.heap[self._get_right_index(i)]


def test_min_heap():
    min_heap = MinHeap([3, 1, 4])
    assert min_heap.pop() == 1
    assert min_heap.pop() == 3
    assert min_heap.pop() == 4
    assert len(min_heap) == 0

    min_heap.push(5)
    min_heap.push(2)
    min_heap.push(4)
    assert min_heap.pop() == 2
    assert min_heap.pop() == 4
    assert min_heap.pop() == 5
