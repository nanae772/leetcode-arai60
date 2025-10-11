# 最初の家と最後の家を無視する場合分けによる解法
class Solution:
    def rob(self, nums: list[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        def rob_in_line(left, right):
            max_robbed_previous = 0
            max_skipped_previous = 0
            for num in nums[left:right]:
                max_robbed_current = max_skipped_previous + num
                max_skipped_previous = max(max_robbed_previous, max_skipped_previous)
                max_robbed_previous = max_robbed_current
            return max(max_robbed_previous, max_skipped_previous)

        max_when_first_skipped = rob_in_line(1, len(nums))
        max_when_last_skipped = rob_in_line(0, len(nums) - 1)
        return max(max_when_first_skipped, max_when_last_skipped)
