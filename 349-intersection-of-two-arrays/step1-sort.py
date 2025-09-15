class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        def create_sorted_unique_list(nums: list[int]) -> list[int]:
            sorted_nums = sorted(nums[:])
            unique_nums = []
            i = 0
            while i < len(sorted_nums):
                if i == len(sorted_nums) - 1 or sorted_nums[i] != sorted_nums[i + 1]:
                    unique_nums.append(sorted_nums[i])
                    i += 1
                    continue
                while i < len(sorted_nums) - 1 and sorted_nums[i] == sorted_nums[i + 1]:
                    i += 1
            return unique_nums

        unique_nums1 = create_sorted_unique_list(nums1)
        unique_nums2 = create_sorted_unique_list(nums2)

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
