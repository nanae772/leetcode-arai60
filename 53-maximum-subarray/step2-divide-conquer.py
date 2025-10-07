class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        def calculate_max_subarray(left: int, right: int) -> int | float:
            if left == right:
                return -float("inf")

            mid = (left + right) // 2
            max_sum_left = calculate_max_subarray(left, mid)
            max_sum_right = calculate_max_subarray(mid + 1, right)

            max_sum_includes_mid = nums[mid]
            sum_ = nums[mid]
            for i in range(mid + 1, right):
                sum_ += nums[i]
                max_sum_includes_mid = max(max_sum_includes_mid, sum_)
            sum_ = max_sum_includes_mid
            for i in reversed(range(left, mid)):
                sum_ += nums[i]
                max_sum_includes_mid = max(max_sum_includes_mid, sum_)

            return max(max_sum_includes_mid, max_sum_left, max_sum_right)

        return calculate_max_subarray(0, len(nums))
