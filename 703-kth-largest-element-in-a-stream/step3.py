import heapq


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.top_k_largest = sorted(nums, reverse=True)[:k]
        heapq.heapify(self.top_k_largest)

    def add(self, val: int) -> int:
        heapq.heappush(self.top_k_largest, val)
        if len(self.top_k_largest) > self.k:
            heapq.heappop(self.top_k_largest)
        return self.top_k_largest[0]
