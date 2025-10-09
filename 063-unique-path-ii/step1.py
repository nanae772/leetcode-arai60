# 貰うDP
class SolutionWithReceivingDP:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        OBSTACLE = 1
        if not obstacleGrid or not obstacleGrid[0]:
            return 0
        if obstacleGrid[0][0] == OBSTACLE:
            return 0

        height = len(obstacleGrid)
        width = len(obstacleGrid[0])
        path_count = [[0] * width for _ in range(height)]
        path_count[0][0] = 1

        for row, col in itertools.product(range(height), range(width)):
            if obstacleGrid[row][col] == OBSTACLE:
                continue

            if row > 0:
                path_count[row][col] += path_count[row - 1][col]
            if col > 0:
                path_count[row][col] += path_count[row][col - 1]

        return path_count[-1][-1]


# 配るDP
class SolutionWithDistributingDP:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        OBSTACLE = 1
        if not obstacleGrid or not obstacleGrid[0]:
            return 0
        if obstacleGrid[0][0] == OBSTACLE:
            return 0

        height = len(obstacleGrid)
        width = len(obstacleGrid[0])
        path_count = [[0] * width for _ in range(height)]
        path_count[0][0] = 1

        for row, col in itertools.product(range(height), range(width)):
            if obstacleGrid[row][col] == OBSTACLE:
                path_count[row][col] = 0
            if row + 1 < height:
                path_count[row + 1][col] += path_count[row][col]
            if col + 1 < width:
                path_count[row][col + 1] += path_count[row][col]

        return path_count[-1][-1]


# メモ化再帰(cache不使用)
class SolutionWithMemoizeRecursion:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        OBSTACLE = 1
        if not obstacleGrid or not obstacleGrid[0]:
            return 0

        height = len(obstacleGrid)
        width = len(obstacleGrid[0])
        path_count = [[None] * width for _ in range(height)]

        def count_path(row: int, col: int) -> int:
            if not (0 <= row < height and 0 <= col < width):
                return 0
            if path_count[row][col] is not None:
                return path_count[row][col]
            if obstacleGrid[row][col] == OBSTACLE:
                path_count[row][col] = 0
                return path_count[row][col]
            if row == 0 and col == 0:
                path_count[row][col] = 1 if obstacleGrid[0][0] != OBSTACLE else 0
                return path_count[row][col]

            path_count[row][col] = count_path(row - 1, col) + count_path(row, col - 1)
            return path_count[row][col]

        return count_path(height - 1, width - 1)
