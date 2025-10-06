class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        if not nums:
            return 0

        lis_length_to_min_value = [-float("inf")]
        for num in nums:
            if lis_length_to_min_value[-1] < num:
                lis_length_to_min_value.append(num)
                continue

            index_update = bisect.bisect_left(lis_length_to_min_value, num)
            lis_length_to_min_value[index_update] = num

        return len(lis_length_to_min_value) - 1
