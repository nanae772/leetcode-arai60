class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        value_to_leftmost_index: dict[int, int] = dict()

        for i in range(len(nums)):
            if target - nums[i] in value_to_leftmost_index:
                return [value_to_leftmost_index[target - nums[i]], i]
            if nums[i] not in value_to_leftmost_index:
                value_to_leftmost_index[nums[i]] = i

        return [-1, -1]
