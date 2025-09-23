class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        height = len(grid)
        width = len(grid[0])
        offsets = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        islands_connection = UnionFind(height * width)
        for row in range(height):
            for col in range(width):
                if grid[row][col] == "0":
                    continue
                for row_offset, col_offset in offsets:
                    next_row = row + row_offset
                    next_col = col + col_offset
                    if not (0 <= next_row < height and 0 <= next_col < width):
                        continue
                    if grid[next_row][next_col] == "0":
                        continue
                    islands_connection.merge(
                        row * width + col, next_row * width + next_col
                    )

        number_islands = 0
        for row in range(height):
            for col in range(width):
                if grid[row][col] == "0":
                    continue
                point = row * width + col
                if islands_connection._root(point) == point:
                    number_islands += 1
        return number_islands


class UnionFind:
    def __init__(self, size: int):
        self.size = size
        self.parent = [-1] * self.size

    def is_same(self, x: int, y: int) -> bool:
        return self._root(x) == self._root(y)

    def merge(self, x: int, y: int) -> None:
        x = self._root(x)
        y = self._root(y)

        if x == y:
            return
        if self._get_size(x) < self._get_size(y):
            x, y = y, x

        self.parent[y] = x
        self.parent[x] = -(self._get_size(x) + self._get_size(y))

    def _root(self, x: int) -> int:
        if self.parent[x] < 0:
            return x
        self.parent[x] = self._root(self.parent[x])
        return self.parent[x]

    def _get_size(self, x: int) -> int:
        x = self._root(x)
        return -self.parent[x]
