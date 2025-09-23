from itertools import product


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        def is_water(row: int, col: int) -> bool:
            return not (0 <= row < height and 0 <= col < width) or grid[row][col] == "0"

        def visit_connected_islands(row: int, col: int) -> None:
            is_visited[row][col] = True
            next_islands = [(row, col)]
            offsets = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            while next_islands:
                row, col = next_islands.pop()
                for row_offset, col_offset in offsets:
                    next_row = row + row_offset
                    next_col = col + col_offset
                    if is_water(next_row, next_col) or is_visited[next_row][next_col]:
                        continue
                    next_islands.append((next_row, next_col))
                    is_visited[next_row][next_col] = True

        height = len(grid)
        width = len(grid[0])
        is_visited = [[False] * width for _ in range(height)]
        number_islands = 0
        for row, col in product(range(height), range(width)):
            if is_water(row, col) or is_visited[row][col]:
                continue
            visit_connected_islands(row, col)
            number_islands += 1
        return number_islands
