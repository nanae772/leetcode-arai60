from itertools import product


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        def is_water(row: int, col: int) -> bool:
            return not (0 <= row < height and 0 <= col < width) or grid[row][col] == "0"

        def connect_surrouding_islands(row: int, col: int) -> None:
            offsets = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for row_offset, col_offset in offsets:
                next_row = row + row_offset
                next_col = col + col_offset
                if is_water(next_row, next_col):
                    continue
                islands_connection.merge(row * width + col, next_row * width + next_col)

        height = len(grid)
        width = len(grid[0])
        islands_connection = UnionFind(height * width)
        number_water = 0
        for row, col in product(range(height), range(width)):
            if is_water(row, col):
                number_water += 1
                continue
            connect_surrouding_islands(row, col)
        number_islands = islands_connection.count_connected_component() - number_water
        return number_islands


class UnionFind:
    """連結成分を管理するクラス"""

    def __init__(self, size: int):
        self.size = size
        self.parent = list(range(self.size))
        self.tree_size = [1] * self.size
        self.number_of_trees = self.size

    def is_same(self, x: int, y: int) -> bool:
        """2つの属する連結成分が等しいか判定する"""
        return self._find_root(x) == self._find_root(y)

    def merge(self, x: int, y: int) -> None:
        """2つの属する連結成分を連結する"""
        x = self._find_root(x)
        y = self._find_root(y)

        if x == y:
            return
        if self.tree_size[x] < self.tree_size[y]:
            x, y = y, x

        self.parent[y] = x
        self.tree_size[x] += self.tree_size[y]
        self.number_of_trees -= 1

    def count_connected_component(self) -> int:
        """現在の連結成分の個数を数える"""
        return self.number_of_trees

    def _find_root(self, x: int) -> int:
        root = x
        nodes = []
        while root != self.parent[root]:
            nodes.append(root)
            root = self.parent[root]
        while nodes:
            self.parent[nodes.pop()] = root
        return root
