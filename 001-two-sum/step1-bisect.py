import bisect


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        value_index_pairs = [(value, index) for index, value in enumerate(nums)]
        value_index_pairs.sort()
        for value, index in value_index_pairs:
            diff = target - value
            left_at_least_diff = bisect.bisect_left(value_index_pairs, (diff, -1))
            if left_at_least_diff >= len(value_index_pairs):
                continue

            v, i = value_index_pairs[left_at_least_diff]
            if diff == v and index != i:
                return [index, i]

        return [-1, -1]
