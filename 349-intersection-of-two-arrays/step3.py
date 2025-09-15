from itertools import groupby


class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        unique_nums1 = [num for num, _ in groupby(sorted(nums1))]
        unique_nums2 = [num for num, _ in groupby(sorted(nums2))]

        intersection_nums = []
        i1, i2 = 0, 0

        while i1 < len(unique_nums1) and i2 < len(unique_nums2):
            if unique_nums1[i1] == unique_nums2[i2]:
                intersection_nums.append(unique_nums1[i1])
                i1 += 1
                i2 += 1
                continue
            if unique_nums1[i1] < unique_nums2[i2]:
                i1 += 1
            else:
                i2 += 1

        return intersection_nums
