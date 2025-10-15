class SolutionBoundary:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # left, right は要素間の境界を指しているとみなす
        left = 0  # a[0], ..., a[left - 1] < target
        right = len(nums)  # a[right], ..., a[-1] >= target

        while left < right:
            mid = (left + right) // 2
            if target <= nums[mid]:
                right = mid
            else:
                left = mid + 1

        return right


class SolutionIndex:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # left, right は要素のindexを指しているとみなす
        left = -1  # a[0], ..., a[left] < target
        right = len(nums)  # a[right], ..., a[-1] >= target

        while left + 1 < right:
            mid = (left + right) // 2
            if target <= nums[mid]:
                right = mid
            else:
                left = mid

        return right


class SolutionRange:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # 未探索区間[left, right)を狭めていく
        # leftより左はtargetより小さいことが確定
        # rightから右はtarget以上であることが確定
        # [left, right)が空、すなわち left = right になるまでやる
        left = 0
        right = len(nums)

        while left < right:
            mid = (left + right) // 2
            if target <= nums[mid]:
                right = mid
            else:
                left = mid + 1

        return right
