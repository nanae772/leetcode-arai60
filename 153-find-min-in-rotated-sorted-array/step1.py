class Solution:
    def findMin(self, nums: list[int]) -> int:
        if not nums:
            raise ValueError("nums must not be empty.")

        front = nums[0]
        left = 0  # これより下はfront以上
        right = len(nums) - 1  # これより上はfront未満

        while left <= right:
            middle = (left + right) // 2
            if nums[middle] >= front:
                left = middle + 1
            else:
                right = middle - 1

        if right + 1 == len(nums):
            return front

        return nums[right + 1]
