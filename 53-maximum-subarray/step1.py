class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        prefix_sum = 0
        min_prefix_sum = 0
        max_sum_subarray = -float("inf")

        for num in nums:
            prefix_sum += num
            max_sum_subarray = max(max_sum_subarray, prefix_sum - min_prefix_sum)
            min_prefix_sum = min(min_prefix_sum, prefix_sum)

        return max_sum_subarray
