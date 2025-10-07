class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m <= 0 or n <= 0:
            return 0

        number_of_path = [[0] * n for _ in range(m)]
        number_of_path[0] = [1] * n
        for i in range(1, m):
            for j in range(n):
                number_of_path[i][j] = number_of_path[i - 1][j]
                if j > 0:
                    number_of_path[i][j] += number_of_path[i][j - 1]
        return number_of_path[m - 1][n - 1]
