class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m <= 0 or n <= 0:
            return 0

        count_path = [[1] * n for _ in range(m)]
        for row, col in itertools.product(range(1, m), range(1, n)):
            count_path[row][col] = count_path[row - 1][col] + count_path[row][col - 1]

        return count_path[m - 1][n - 1]
