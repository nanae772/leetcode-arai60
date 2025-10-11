class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) <= 2:
            return max(nums, default=0)

        def rob_in_line(moneys: list[int]) -> int:
            max_robbed_previous = 0
            max_skipped_previous = 0
            for money in moneys:
                max_robbed_current = max_skipped_previous + money
                max_skipped_previous = max(max_robbed_previous, max_skipped_previous)
                max_robbed_previous = max_robbed_current

            return max(max_robbed_previous, max_skipped_previous)

        max_when_robbed_first = nums[0] + rob_in_line(nums[2:-1])
        max_when_skipped_first = rob_in_line(nums[1:])
        return max(max_when_robbed_first, max_when_skipped_first)
