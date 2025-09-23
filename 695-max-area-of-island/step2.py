class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        # 空盤面に対する例外処理
        if not grid or not grid[0]:
            return 0

        height = len(grid)
        width = len(grid[0])
        is_explored = [[False] * width for _ in range(height)]

        def is_frontier(row: int, col: int) -> bool:
            return (
                (0 <= row < height and 0 <= col < width)
                and grid[row][col] == 1
                and not is_explored[row][col]
            )

        def measure_island(row: int, col: int) -> int:
            if not is_frontier(row, col):
                return 0

            is_explored[row][col] = True
            offsets = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            area = 1
            for row_offset, col_offset in offsets:
                area += measure_island(row + row_offset, col + col_offset)
            return area

        max_area = 0
        for row, col in product(range(height), range(width)):
            if is_frontier(row, col):
                max_area = max(max_area, measure_island(row, col))
        return max_area
