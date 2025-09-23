class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        sum_to_count = {0: 1}
        prefix_sum = 0
        count_subarray_sum_k = 0
        for num in nums:
            prefix_sum += num
            complement = prefix_sum - k
            if complement in sum_to_count:
                count_subarray_sum_k += sum_to_count[complement]
            if prefix_sum not in sum_to_count:
                sum_to_count[prefix_sum] = 1
            else:
                sum_to_count[prefix_sum] += 1
        return count_subarray_sum_k
