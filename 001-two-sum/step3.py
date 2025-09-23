class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        value_to_leftmost_index = dict()
        for index, value in enumerate(nums):
            diff = target - value
            if diff in value_to_leftmost_index:
                return [value_to_leftmost_index[diff], index]
            if value not in value_to_leftmost_index:
                value_to_leftmost_index[value] = index

        return [-1, -1]
