import dataclasses
from collections import Counter
from random import randint


@dataclasses.dataclass
class ValueCount:
    value: int
    count: int


# Quickselect with Dutch natinal flag partition
# https://en.wikipedia.org/wiki/Dutch_national_flag_problem
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        def select_top_k_frequent(left: int, right: int) -> list[ValueCount]:
            def swap(i0: int, i1: int) -> None:
                value_counts[i0], value_counts[i1] = value_counts[i1], value_counts[i0]

            def dutch_national_flag_partition(index_pivot: int) -> tuple[int, int]:
                # [<pivot], [=pivot], [>pivot] となるように区間を三分割する
                pivot_count = value_counts[index_pivot].count

                # [left .. left_equals_to_pivot - 1]              : pivotより小さい
                # [left_equals_to_pivot .. left_unsorted - 1]     : pivotに等しい
                # [left_unsorted .. left_greather_than_pivot - 1] : 未整理
                # [left_greather_than_pivot .. right]             : pivotより大きい
                left_equals_to_pivot = left
                left_unsorted = left
                left_greather_than_pivot = right + 1

                while left_unsorted < left_greather_than_pivot:
                    if value_counts[left_unsorted].count < pivot_count:
                        swap(left_unsorted, left_equals_to_pivot)
                        left_equals_to_pivot += 1
                        left_unsorted += 1
                        continue
                    if value_counts[left_unsorted].count > pivot_count:
                        left_greather_than_pivot -= 1
                        swap(left_unsorted, left_greather_than_pivot)
                        continue
                    assert value_counts[left_unsorted].count == pivot_count
                    left_unsorted += 1

                assert left_equals_to_pivot < left_greather_than_pivot
                return left_equals_to_pivot, left_greather_than_pivot - 1

            assert 0 <= left <= right < len(value_counts)
            index_pivot = randint(left, right)
            left_equals_to_pivot, right_equals_to_pivot = dutch_national_flag_partition(
                index_pivot
            )
            if left_equals_to_pivot <= len(value_counts) - k <= right_equals_to_pivot:
                return value_counts[len(value_counts) - k :]
            if left_equals_to_pivot > len(value_counts) - k:
                return select_top_k_frequent(left, left_equals_to_pivot - 1)
            assert right_equals_to_pivot < len(value_counts) - k
            return select_top_k_frequent(right_equals_to_pivot + 1, right)

        value_counts = [
            ValueCount(value, count) for value, count in Counter(nums).items()
        ]
        top_k_frequent = select_top_k_frequent(0, len(value_counts) - 1)
        return [value_count.value for value_count in top_k_frequent]
