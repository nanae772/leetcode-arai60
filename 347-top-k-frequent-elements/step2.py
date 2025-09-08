from collections import Counter
from dataclasses import dataclass
from random import randint


@dataclass
class ValueCount:
    value: int
    count: int


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        def swap(i0: int, i1: int) -> None:
            assert 0 <= i0 < len(value_counts)
            assert 0 <= i1 < len(value_counts)
            value_counts[i0], value_counts[i1] = value_counts[i1], value_counts[i0]

        def select_top_k_frequent(left: int, right: int) -> List[int]:
            def my_partition(left: int, right: int, index_pivot: int) -> int:
                # 自分で考えた分割アルゴリズム
                # pivotを一旦右端に持っていき左はpivot以上、右はpivot未満になるように分ける
                pivot_count = value_counts[index_pivot].count
                swap(index_pivot, right)
                rightmost_at_least_pivot = right
                leftmost_less_than_pivot = left
                while leftmost_less_than_pivot < rightmost_at_least_pivot:
                    if value_counts[rightmost_at_least_pivot - 1].count < pivot_count:
                        swap(rightmost_at_least_pivot - 1, rightmost_at_least_pivot)
                        rightmost_at_least_pivot -= 1
                        continue
                    swap(leftmost_less_than_pivot, rightmost_at_least_pivot - 1)
                    leftmost_less_than_pivot += 1
                return rightmost_at_least_pivot

            def lomutos_partition(left: int, right: int, index_pivot: int) -> int:
                # Lomutoの分割アルゴリズム
                # https://en.wikipedia.org/wiki/Quicksort#Lomuto_partition_scheme
                # pivotを一旦右端に持っていき左はpivot以上、右はpivot未満になるように分ける
                pivot_count = value_counts[index_pivot].count
                swap(index_pivot, right)
                rightmost_at_least_pivot = right
                leftmost_less_than_pivot = left
                for i in range(left, right):
                    if value_counts[i].count >= pivot_count:
                        swap(leftmost_less_than_pivot, i)
                        leftmost_less_than_pivot += 1
                swap(leftmost_less_than_pivot, rightmost_at_least_pivot)
                rightmost_at_least_pivot = leftmost_less_than_pivot
                return rightmost_at_least_pivot

            def hoares_partition(left: int, right: int, index_pivot: int) -> int:
                # Hoareの分割アルゴリズム
                # https://en.wikipedia.org/wiki/Quicksort#Hoare_partition_scheme
                # 左側はpivot以上、右側はpivot以下になるように分ける
                pivot_count = value_counts[index_pivot].count
                leftmost_at_most_pivot = left - 1
                rightmost_at_least_pivot = right + 1

                while True:
                    leftmost_at_most_pivot += 1
                    while value_counts[leftmost_at_most_pivot].count > pivot_count:
                        leftmost_at_most_pivot += 1

                    rightmost_at_least_pivot -= 1
                    while value_counts[rightmost_at_least_pivot].count < pivot_count:
                        rightmost_at_least_pivot -= 1

                    if leftmost_at_most_pivot >= rightmost_at_least_pivot:
                        return rightmost_at_least_pivot
                    swap(leftmost_at_most_pivot, rightmost_at_least_pivot)

                assert False, "Unreachable"

            assert 0 <= left <= right < len(value_counts)
            index_pivot = randint(left, right)
            rightmost_at_least_pivot = hoares_partition(left, right, index_pivot)
            if rightmost_at_least_pivot == k - 1:
                return value_counts[:k]
            if rightmost_at_least_pivot < k - 1:
                return select_top_k_frequent(rightmost_at_least_pivot + 1, right)
            return select_top_k_frequent(left, rightmost_at_least_pivot)

        value_counts = [
            ValueCount(value, count) for value, count in Counter(nums).items()
        ]
        top_k_frequent = select_top_k_frequent(0, len(value_counts) - 1)
        return [value_count.value for value_count in top_k_frequent]
