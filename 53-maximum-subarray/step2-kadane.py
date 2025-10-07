# Kadane's algorithm
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        sum_ = nums[0]
        max_sum = sum_
        for num in nums[1:]:
            sum_ = max(sum_ + num, num)
            max_sum = max(max_sum, sum_)
        return max_sum
