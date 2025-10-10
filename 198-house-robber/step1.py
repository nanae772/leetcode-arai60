# 長さNの配列を使ってDPで解く方法
class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        max_money = [0] * len(nums)
        max_money[0] = nums[0]
        max_money[1] = max(max_money[0], nums[1])
        for i in range(2, len(nums)):
            max_money[i] = max(max_money[i - 1], max_money[i - 2] + nums[i])
        return max_money[-1]


# 計算量削減のため、２つの変数だけで行うDP
class SolutionOnlyTwoVariables:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        max_end_at_current = max(nums[0], nums[1])
        max_end_at_previous = nums[0]
        for num in nums[2:]:
            max_end_at_current, max_end_at_previous = (
                max(max_end_at_current, max_end_at_previous + num),
                max_end_at_current,
            )
        return max_end_at_current
