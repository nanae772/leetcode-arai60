class SolutionTwoBS:
    def search(self, nums: list[int], target: int) -> int:
        if not nums:
            return -1

        def find_min_index() -> int:
            """numsの最小値を指すindexを見つける"""
            lo = 0  # これより下はnums[-1]より大きい
            hi = len(nums)  # これ以上はnums[-1]以下

            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] <= nums[-1]:
                    hi = mid
                else:
                    lo = mid + 1

            return hi

        def find_target_index(left: int, right: int) -> int:
            """nums[left:right]の中からtargetを指すindexを見つける
            無ければ-1を返す
            """
            lo = left  # これより下はtarget未満
            hi = right  # これ以上はtarget以上
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] >= target:
                    hi = mid
                else:
                    lo = mid + 1

            if hi == right or nums[hi] != target:
                return -1
            return hi

        min_index = find_min_index()
        if target <= nums[-1]:
            return find_target_index(min_index, len(nums))
        else:
            return find_target_index(0, min_index)


class SolutionWithOffset:
    def search(self, nums: list[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1
        offset = 10**5  # numsの最大値と最小値以上の値なら何でもよい
        if target <= nums[-1]:
            target += offset

        while lo <= hi:
            mid = (lo + hi) // 2
            fixed_num_mid = nums[mid]
            if nums[mid] <= nums[-1]:
                fixed_num_mid += offset

            if fixed_num_mid == target:
                return mid
            if fixed_num_mid < target:
                lo = mid + 1
            else:
                hi = mid - 1

        return -1


class SolutionOneBS:
    def search(self, nums: list[int], target: int) -> int:
        def can_exists_in_range(left: int, right: int) -> bool:
            if left > right:
                return False
            if nums[left] <= nums[right]:
                return nums[left] <= target <= nums[right]
            else:
                return nums[left] <= target or target <= nums[right]

        lo = 0
        hi = len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid

            if can_exists_in_range(lo, mid - 1):
                hi = mid - 1
            else:
                lo = mid + 1

        return -1
