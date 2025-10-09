class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        if not obstacleGrid or not obstacleGrid[0]:
            return 0

        OBSTACLE = 1
        if obstacleGrid[0][0] == OBSTACLE:
            return 0

        height = len(obstacleGrid)
        width = len(obstacleGrid[0])
        count_path_in_row = [0] * width

        for row, col in itertools.product(range(height), range(width)):
            if (row, col) == (0, 0):
                count_path_in_row[0] = 1
                continue
            if obstacleGrid[row][col] == OBSTACLE:
                count_path_in_row[col] = 0
                continue

            from_above = count_path_in_row[col]
            from_left = count_path_in_row[col - 1] if col > 0 else 0
            count_path_in_row[col] = from_above + from_left

        return count_path_in_row[-1]
