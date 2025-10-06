class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        if not nums:
            return 0

        max_length_increasing_subseq = [1] * len(nums)
        for i in range(len(nums)):
            max_length_pre = max(
                (
                    max_length_increasing_subseq[j]
                    for j in range(0, i)
                    if nums[j] < nums[i]
                ),
                default=0,
            )
            max_length_increasing_subseq[i] = max_length_pre + 1

        return max(max_length_increasing_subseq)
