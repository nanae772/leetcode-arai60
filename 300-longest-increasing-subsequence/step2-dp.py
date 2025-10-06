class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        if not nums:
            return 0

        end_index_to_lis_length = [1] * len(nums)
        for i in range(len(nums)):
            end_index_to_lis_length[i] = (
                max(
                    (
                        end_index_to_lis_length[j]
                        for j in range(0, i)
                        if nums[j] < nums[i]
                    ),
                    default=0,
                )
                + 1
            )

        return max(end_index_to_lis_length)
