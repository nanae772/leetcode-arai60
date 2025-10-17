class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if not nums:
            return -1

        def find_min_index() -> int:
            lo = 0
            hi = len(nums)
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] <= nums[-1]:
                    hi = mid
                else:
                    lo = mid + 1
            return hi

        def find_target_index_in_sorted_range(left: int, right: int) -> int:
            lo = left
            hi = right
            while lo < hi:
                mid = (lo + hi) // 2
                if target <= nums[mid]:
                    hi = mid
                else:
                    lo = mid + 1

            if hi == right or nums[hi] != target:
                return -1
            return hi

        min_index = find_min_index()
        if target <= nums[-1]:
            return find_target_index_in_sorted_range(min_index, len(nums))
        else:
            return find_target_index_in_sorted_range(0, min_index)
