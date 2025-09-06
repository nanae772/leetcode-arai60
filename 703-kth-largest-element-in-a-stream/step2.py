class KthLargest:
    """K番目に大きい値を保持するデータ構造"""

    def __init__(self, k: int, nums: List[int]):
        if k <= 0:
            raise ValueError(f"k must be >= 1 (got k={k}).")

        self.k = k
        self.top_k_largest = MinHeap(sorted(nums, reverse=True)[:k], k + 1)

    def add(self, val: int) -> int:
        """valを挿入し、その後K番目に大きい値を返す"""
        self.top_k_largest.push(val)
        if len(self.top_k_largest) < self.k:
            raise IndexError(
                "cannot determine the k-th value because there are fewer than k elements"
                f" (size={len(self.top_k_largest)}, k={self.k})."
            )
        if len(self.top_k_largest) > self.k:
            self.top_k_largest.pop()
        return self.top_k_largest.peek()


class MinHeap:
    """最小ヒープ"""

    def __init__(self, array: list[int] = [], capacity: int = None) -> None:
        if capacity is None:
            capacity = len(array)
        if capacity <= 0:
            raise ValueError(f"capacity must be >= 1 (got capacity={capacity}).")
        if capacity < len(array):
            raise ValueError(
                "capacity must be greater than or equal to the length of the array"
                f"(capacity={capacity}, len(array)={len(array)})."
            )

        self.capacity = capacity
        self.length = len(array)
        self.heap = array[:] + [float("inf")] * (capacity - self.length)
        # self.heapをヒープ化する
        for i in reversed(range(self.length)):
            self._heapify_subtree(i)

    def __len__(self):
        return self.length

    def peek(self) -> int:
        """ヒープ内の最小の値を返す"""
        if self.length == 0:
            raise IndexError("heap is empty.")
        return self.heap[0]

    def push(self, val: int) -> None:
        """ヒープにvalを挿入する"""
        if self.length == self.capacity:
            raise IndexError("heap is full.")

        self.heap[self.length] = val
        i = self.length
        self.length += 1

        while i > 0 and self.heap[i] < self.heap[(i - 1) // 2]:
            self._swap(i, (i - 1) // 2)
            i = (i - 1) // 2

    def pop(self) -> int:
        """ヒープから最小の値を取り出し、その値を返す"""
        if self.length == 0:
            raise IndexError("heap is empty.")
        if self.length == 1:
            self.length = 0
            return self.heap[0]

        top = self.heap[0]
        self._swap(0, self.length - 1)
        self.length -= 1
        self._heapify_subtree(0)
        return top

    def _swap(self, i: int, j: int) -> None:
        assert 0 <= i < self.length, f"out of range: {i=}"
        assert 0 <= j < self.length, f"out of range: {j=}"
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _heapify_subtree(self, i: int) -> None:
        assert 0 <= i < self.length, f"out of range: {i=}"
        while True:
            left = float("inf")
            if 2 * i + 1 < self.length:
                left = self.heap[2 * i + 1]
            right = float("inf")
            if 2 * i + 2 < self.length:
                right = self.heap[2 * i + 2]

            min_ = min(self.heap[i], left, right)
            if min_ == self.heap[i]:
                return
            if min_ == self.heap[2 * i + 1]:
                self._swap(i, 2 * i + 1)
                i = 2 * i + 1
            else:
                self._swap(i, 2 * i + 2)
                i = 2 * i + 2


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
