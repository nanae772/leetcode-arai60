import dataclasses
from collections import Counter
from random import randint


@dataclasses.dataclass
class ValueCount:
    value: int
    count: int


# Quickselect with Hoare's Partition
# https://en.wikipedia.org/wiki/Quicksort#Hoare_partition_scheme
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        def select_top_k_frequent(left: int, right: int) -> list[ValueCount]:
            def swap(i0: int, i1: int) -> None:
                value_counts[i0], value_counts[i1] = value_counts[i1], value_counts[i0]

            def hoare_partition(index_pivot: int) -> int:
                # 左がpivot以下、右がpivot以上になるように分ける
                pivot_count = value_counts[index_pivot].count
                left_at_least_pivot = left - 1
                right_at_most_pivot = right + 1

                while True:
                    left_at_least_pivot += 1
                    while value_counts[left_at_least_pivot].count < pivot_count:
                        left_at_least_pivot += 1
                    right_at_most_pivot -= 1
                    while value_counts[right_at_most_pivot].count > pivot_count:
                        right_at_most_pivot -= 1

                    if left_at_least_pivot >= right_at_most_pivot:
                        return left_at_least_pivot

                    swap(left_at_least_pivot, right_at_most_pivot)

                assert False, "Unreachable"

            assert 0 <= left <= right < len(value_counts)
            if left == right:
                assert left == len(value_counts) - k
                return value_counts[len(value_counts) - k :]

            # 確実に区間を狭めるため左端がpivotにならないようにする
            index_pivot = randint(left + 1, right)
            left_at_least_pivot = hoare_partition(index_pivot)
            if left_at_least_pivot == len(value_counts) - k:
                return value_counts[len(value_counts) - k :]
            if left_at_least_pivot < len(value_counts) - k:
                return select_top_k_frequent(left_at_least_pivot, right)
            return select_top_k_frequent(left, left_at_least_pivot - 1)

        value_counts = [
            ValueCount(value, count) for value, count in Counter(nums).items()
        ]
        top_k_frequent = select_top_k_frequent(0, len(value_counts) - 1)
        return [value_count.value for value_count in top_k_frequent]
