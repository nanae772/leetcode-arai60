class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if n <= 0 or m <= 0:
            return 0
        return math.comb(m + n - 2, m - 1)
