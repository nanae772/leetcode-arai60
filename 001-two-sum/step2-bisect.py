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

            min_value_at_least_diff, min_index_at_least_diff = value_index_pairs[
                left_at_least_diff
            ]
            if min_value_at_least_diff == diff and min_index_at_least_diff != index:
                return sorted([index, min_index_at_least_diff])

        return [-1, -1]
