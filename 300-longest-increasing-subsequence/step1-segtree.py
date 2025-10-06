class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        if not nums:
            return 0

        def compress(nums: list[int]) -> list[int]:
            """numsの大小関係を維持しつつ、小さいほうから0,1,2...と値を圧縮する"""
            compressed_nums = [None] * len(nums)
            num_index_pair_sorted = sorted((num, i) for i, num in enumerate(nums))
            compressed_num = -1
            previous = -float("inf")
            for num, i in num_index_pair_sorted:
                if num != previous:
                    compressed_num += 1
                compressed_nums[i] = compressed_num
                previous = num

            return compressed_nums

        compressed_nums = compress(nums)
        max_length_increasing_subseq = MaxSegmentTree(len(compressed_nums))
        result = 1

        for i in range(len(compressed_nums)):
            max_length_i = (
                max_length_increasing_subseq.range_max(0, compressed_nums[i]) + 1
            )
            max_length_increasing_subseq.update(compressed_nums[i], max_length_i)
            result = max(result, max_length_i)

        return result


class MaxSegmentTree:
    def __init__(self, size: int):
        self.size = 1
        # 簡単のため、size以上の最も近い2のべき乗をself.sizeとする
        while self.size < size:
            self.size *= 2
        self.values = [0] * (2 * self.size - 1)

    def _parent_index(self, i: int) -> int:
        return (i - 1) // 2

    def _left_index(self, i: int) -> int:
        return 2 * i + 1

    def _right_index(self, i: int) -> int:
        return 2 * i + 2

    def range_max(self, left: int, right: int) -> int:
        return self._range_max_helper(left, right, 0, self.size, 0)

    def _range_max_helper(
        self, left: int, right: int, begin: int, end: int, pos: int
    ) -> int:
        """クエリ区間[left, right)に対して、区間[begin, end)で重なる最大値を返す"""
        if not left < right:  # 無効な区間
            return 0
        if end <= left or right <= begin:  # 重なりが無い
            return 0
        if left <= begin and end <= right:
            # [begin, end)が完全に[left, right)に含まれる
            return self.values[pos]

        mid = (begin + end) // 2
        return max(
            self._range_max_helper(left, right, begin, mid, self._left_index(pos)),
            self._range_max_helper(left, right, mid, end, self._right_index(pos)),
        )

    def update(self, i: int, value: int) -> None:
        """i番目のデータをmax(values[i], value)に更新する"""
        i = i + self.size - 1
        self.values[i] = max(self.values[i], value)
        while i > 0:
            i = self._parent_index(i)
            self.values[i] = max(self.values[i], value)
