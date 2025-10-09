class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        if not obstacleGrid or not obstacleGrid[0]:
            return 0

        OBSTACLE = 1
        if obstacleGrid[0][0] == OBSTACLE:
            return 0

        height = len(obstacleGrid)
        width = len(obstacleGrid[0])
        path_count_in_row = [0] * width
        for row, col in itertools.product(range(height), range(width)):
            if obstacleGrid[row][col] == OBSTACLE:
                path_count_in_row[col] = 0
                continue
            if (row, col) == (0, 0):
                path_count_in_row[0] = 1
                continue

            path_count_from_above = path_count_in_row[col]
            path_count_from_left = path_count_in_row[col - 1] if col > 0 else 0
            path_count_in_row[col] = path_count_from_above + path_count_from_left

        return path_count_in_row[-1]
