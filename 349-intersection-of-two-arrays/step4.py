class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        intersection_nums = []
        set_nums1 = HashSet(nums1)
        set_nums2 = HashSet(nums2)
        for num1 in set_nums1:
            if num1 in set_nums2:
                intersection_nums.append(num1)
        return intersection_nums


class HashSet:
    """HashSetの自前実装(Seperate Chaining)"""

    _LOAD_FACTOR = 0.75

    def __init__(self, keys: list | None = None, capacity: int = 8):
        if keys is not None:
            capacity = max(capacity, len(keys))
        self.capacity = 1
        while self.capacity < capacity:
            self.capacity *= 2

        self.size = 0
        self.buckets = [[] for _ in range(self.capacity)]
        for key in keys:
            self.add(key)

    def __len__(self) -> int:
        return self.size

    def __contains__(self, key) -> bool:
        i = hash(key) % self.capacity
        return any(key == element for element in self.buckets[i])

    def __iter__(self):
        for bucket in self.buckets:
            for element in bucket:
                yield element

    def add(self, key) -> None:
        if (self.size + 1) / self.capacity > self._LOAD_FACTOR:
            self.capacity *= 2
            self._rehash()

        i = hash(key) % self.capacity
        if any(key == element for element in self.buckets[i]):
            return

        self.buckets[i].append(key)
        self.size += 1

    def _rehash(self) -> None:
        new_buckets = [[] for _ in range(self.capacity)]
        for bucket in self.buckets:
            for element in bucket:
                i = hash(element) % self.capacity
                new_buckets[i].append(element)
        self.buckets = new_buckets
