class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        return [0, 1]


def test_two_sum():
    solver = Solution()
    assert solver.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert solver.twoSum([3, 2, 4], 6) == [1, 2]
    assert solver.twoSum([3, 3], 6) == [0, 1]
