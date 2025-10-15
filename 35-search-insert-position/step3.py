class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)

        while left < right:
            middle = (left + right) // 2
            if target <= nums[middle]:
                right = middle
            else:
                left = middle + 1

        return right
