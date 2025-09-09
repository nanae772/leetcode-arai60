import dataclasses
from collections import Counter
from random import randint


@dataclasses.dataclass
class ValueCount:
    value: int
    count: int


# Quickselect with Lomuto's Partition
# https://en.wikipedia.org/wiki/Quicksort#Lomuto_partition_scheme
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        def select_top_k_frequent(left: int, right: int) -> list[ValueCount]:
            def swap(i0: int, i1: int) -> None:
                value_counts[i0], value_counts[i1] = value_counts[i1], value_counts[i0]

            def lomutos_partition(index_pivot: int) -> int:
                # 左をpivot未満、右をpivot以上に分ける
                pivot_count = value_counts[index_pivot].count
                swap(index_pivot, right)
                left_at_least_pivot = left
                for i in range(left, right):
                    if value_counts[i].count < pivot_count:
                        swap(i, left_at_least_pivot)
                        left_at_least_pivot += 1
                swap(left_at_least_pivot, right)
                return left_at_least_pivot

            assert 0 <= left <= right < len(value_counts)
            index_pivot = randint(left, right)
            left_at_least_pivot = lomutos_partition(index_pivot)
            if left_at_least_pivot == len(value_counts) - k:
                return value_counts[len(value_counts) - k :]
            if left_at_least_pivot < len(value_counts) - k:
                return select_top_k_frequent(left_at_least_pivot + 1, right)
            return select_top_k_frequent(left, left_at_least_pivot - 1)

        value_counts = [
            ValueCount(value, count) for value, count in Counter(nums).items()
        ]
        top_k_frequent = select_top_k_frequent(0, len(value_counts) - 1)
        return [value_count.value for value_count in top_k_frequent]
