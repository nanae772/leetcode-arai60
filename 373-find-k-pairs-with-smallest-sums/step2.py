from dataclasses import dataclass, field
from heapq import heappop, heappush


@dataclass(order=True)
class PairSum:
    i: int = field(compare=False)
    j: int = field(compare=False)
    sum_: int


class Solution:
    def kSmallestPairs(
        self, nums1: list[int], nums2: list[int], k: int
    ) -> list[list[int]]:
        def check_and_add(i: int, j: int) -> None:
            if i >= len(nums1) or j >= len(nums2) or (i, j) in seen_pairs:
                return
            heappush(pair_sums, PairSum(i, j, nums1[i] + nums2[j]))
            seen_pairs.add((i, j))

        pair_sums = [PairSum(0, 0, nums1[0] + nums2[0])]
        seen_pairs = set((0, 0))
        k_smallest = []

        for _ in range(k):
            pair_sum = heappop(pair_sums)
            k_smallest.append([nums1[pair_sum.i], nums2[pair_sum.j]])
            check_and_add(pair_sum.i + 1, pair_sum.j)
            check_and_add(pair_sum.i, pair_sum.j + 1)

        return k_smallest
