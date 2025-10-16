import bisect


class Solution:
    def findMin(self, nums: list[int]) -> int:
        min_index = bisect.bisect_left(nums, True, key=lambda x: x <= nums[-1])
        return nums[min_index]
