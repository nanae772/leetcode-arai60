from heapq import heappop, heappush


class Solution:
    def kSmallestPairs(
        self, nums1: list[int], nums2: list[int], k: int
    ) -> list[list[int]]:
        def check_and_add(i1: int, i2: int) -> None:
            if i1 >= len(nums1) or i2 >= len(nums2) or (i1, i2) in seen_pairs:
                return
            heappush(sum_pairs, (nums1[i1] + nums2[i2], i1, i2))
            seen_pairs.add((i1, i2))

        k_smallest = []
        sum_pairs = [(nums1[0] + nums2[0], 0, 0)]
        seen_pairs = set((0, 0))

        for _ in range(k):
            _sum, i1, i2 = heappop(sum_pairs)
            k_smallest.append([nums1[i1], nums2[i2]])
            check_and_add(i1 + 1, i2)
            check_and_add(i1, i2 + 1)

        return k_smallest
