class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if not nums:
            return -1

        def find_min() -> int:
            """numsの最小値を指すindexを見つける"""
            left = 0
            right = len(nums)

            while left < right:
                mid = (left + right) // 2
                if nums[mid] <= nums[-1]:
                    right = mid
                else:
                    left = mid + 1

            return right

        def find_target(left: int, right: int) -> int:
            """nums[left:right]の中からtargetを指すindexを見つける
            無ければ-1を返す
            """
            lo = left
            hi = right
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] >= target:
                    hi = mid
                else:
                    lo = mid + 1

            if hi == right or nums[hi] != target:
                return -1
            return hi

        min_index = find_min()
        if target <= nums[-1]:
            return find_target(min_index, len(nums))
        else:
            return find_target(0, min_index)
