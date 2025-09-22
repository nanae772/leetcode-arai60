from collections import defaultdict


class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        prefix_sum_to_count = defaultdict(int, {0: 1})
        prefix_sum = 0
        count_subarray_sum_k = 0
        for num in nums:
            prefix_sum += num
            complement = prefix_sum - k
            count_subarray_sum_k += prefix_sum_to_count[complement]
            prefix_sum_to_count[prefix_sum] += 1
        return count_subarray_sum_k
