from heapq import heappop, heappush


class Solution:
    def kSmallestPairs(
        self, nums1: list[int], nums2: list[int], k: int
    ) -> list[list[int]]:
        sum_and_indices = [(nums1[0] + nums2[0], 0, 0)]
        pushed_pairs = set((0, 0))
        smallest_pairs = []

        for _ in range(k):
            assert sum_and_indices, "heap must not be empty."
            sum_pair, index_num1, index_num2 = heappop(sum_and_indices)
            smallest_pairs.append([nums1[index_num1], nums2[index_num2]])

            if (
                index_num1 + 1 < len(nums1)
                and (index_num1 + 1, index_num2) not in pushed_pairs
            ):
                heappush(
                    sum_and_indices,
                    (
                        nums1[index_num1 + 1] + nums2[index_num2],
                        index_num1 + 1,
                        index_num2,
                    ),
                )
                pushed_pairs.add((index_num1 + 1, index_num2))

            if (
                index_num2 + 1 < len(nums2)
                and (index_num1, index_num2 + 1) not in pushed_pairs
            ):
                heappush(
                    sum_and_indices,
                    (
                        nums1[index_num1] + nums2[index_num2 + 1],
                        index_num1,
                        index_num2 + 1,
                    ),
                )
                pushed_pairs.add((index_num1, index_num2 + 1))

        assert len(smallest_pairs) == k
        return smallest_pairs
