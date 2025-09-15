class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        return sorted(set(nums1).intersection(nums2))
