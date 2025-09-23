class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        def is_water(row: int, col: int) -> bool:
            return not (0 <= row < height and 0 <= col < width) or grid[row][col] == 0

        def count_connected_islands(row: int, col: int) -> int:
            is_visited[row][col] = True
            offsets = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            number_islands = 1
            for row_offset, col_offset in offsets:
                next_row = row + row_offset
                next_col = col + col_offset
                if is_water(next_row, next_col) or is_visited[next_row][next_col]:
                    continue
                number_islands += count_connected_islands(next_row, next_col)
            return number_islands

        height = len(grid)
        width = len(grid[0])
        is_visited = [[False] * width for _ in range(height)]
        max_area_of_islands = 0
        for row, col in product(range(height), range(width)):
            if is_water(row, col) or is_visited[row][col]:
                continue
            max_area_of_islands = max(
                max_area_of_islands, count_connected_islands(row, col)
            )
        return max_area_of_islands
