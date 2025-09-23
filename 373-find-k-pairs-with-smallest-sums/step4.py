from heapq import heappop, heappush


class Solution:
    def kSmallestPairs(
        self, nums1: list[int], nums2: list[int], k: int
    ) -> list[list[int]]:
        def push_if_candidate_min_pair(i1: int, i2: int) -> None:
            if i1 >= len(nums1) or i2 >= len(nums2):
                return
            if next_i1[i2] != i1 or next_i2[i1] != i2:
                return
            heappush(candidate_min_pairs, (nums1[i1] + nums2[i2], i1, i2))

        k_smallest_pairs = []
        candidate_min_pairs = [(nums1[0] + nums2[0], 0, 0)]

        # nums2[i2]を選んだときに次の最小ペアの候補となるnums1のインデックスi1
        next_i1 = [0] * len(nums2)
        # nums1[i1]を選んだときに次の最小ペアの候補となるnums2のインデックスi2
        next_i2 = [0] * len(nums1)

        for _ in range(k):
            assert candidate_min_pairs, "heap must not be empty."
            _sum, i1, i2 = heappop(candidate_min_pairs)
            k_smallest_pairs.append([nums1[i1], nums2[i2]])
            next_i1[i2] = i1 + 1
            next_i2[i1] = i2 + 1
            push_if_candidate_min_pair(i1 + 1, i2)
            push_if_candidate_min_pair(i1, i2 + 1)

        return k_smallest_pairs
