class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        def traverse_islands(row: int, col: int) -> None:
            next_islands = [(row, col)]
            while next_islands:
                row, col = next_islands.pop()
                is_visited[row][col] = True
                for row_offset, col_offset in offsets:
                    next_row = row + row_offset
                    next_col = col + col_offset
                    if not (0 <= next_row < height and 0 <= next_col < width):
                        continue
                    if (
                        grid[next_row][next_col] == "0"
                        or is_visited[next_row][next_col]
                    ):
                        continue
                    next_islands.append((next_row, next_col))

        height = len(grid)
        width = len(grid[0])
        is_visited = [[False] * width for _ in range(height)]
        offsets = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        number_islands = 0

        for row in range(height):
            for col in range(width):
                if grid[row][col] == "0" or is_visited[row][col]:
                    continue
                traverse_islands(row, col)
                number_islands += 1

        return number_islands
