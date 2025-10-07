class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        if not nums:
            return 0

        max_subarray_sum = nums[0]
        subarray_sum = 0
        for num in nums:
            subarray_sum = max(subarray_sum + num, num)
            max_subarray_sum = max(max_subarray_sum, subarray_sum)
        return max_subarray_sum
