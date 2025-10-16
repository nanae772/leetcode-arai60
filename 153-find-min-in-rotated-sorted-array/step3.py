class Solution:
    def findMin(self, nums: list[int]) -> int:
        if not nums:
            raise ValueError("nums must not be empty.")

        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] <= nums[-1]:
                right = middle - 1
            else:
                left = middle + 1

        return nums[right + 1]
