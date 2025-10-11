class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) <= 2:
            return max(nums, default=0)

        def calculate_max_robbed_at_line(left: int, right: int) -> int:
            """区間[left, right)に含まれる家が一直線に並んでいる場合に盗める最大値を計算する"""
            max_robbed_previous = 0
            max_skipped_previous = 0
            for num in nums[left:right]:
                max_robbed_current = max_skipped_previous + num
                max_skipped_previous = max(max_robbed_previous, max_skipped_previous)
                max_robbed_previous = max_robbed_current
            return max(max_robbed_previous, max_skipped_previous)

        # 0番目を取ると決めたら直線上の[2, len(nums) - 1)から取る問題に帰着できる
        max_when_robbed_first = nums[0] + calculate_max_robbed_at_line(2, len(nums) - 1)
        # 0番目をスキップすると決めたら直線上の[1, len(nums))から取る問題に帰着できる
        max_when_skipped_first = calculate_max_robbed_at_line(1, len(nums))

        return max(max_when_robbed_first, max_when_skipped_first)
