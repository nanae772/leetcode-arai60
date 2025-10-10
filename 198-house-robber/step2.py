class Solution:
    def rob(self, nums: list[int]) -> int:
        max_robbed_previous = 0
        max_skipped_previous = 0
        for num in nums:
            max_robbed_current = max_skipped_previous + num
            max_skipped_previous = max(max_robbed_previous, max_skipped_previous)
            max_robbed_previous = max_robbed_current

        return max(max_robbed_previous, max_skipped_previous)
