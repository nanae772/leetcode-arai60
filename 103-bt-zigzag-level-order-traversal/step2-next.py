import enum


class Direction(enum.Enum):
    LEFT_TO_RIGHT = enum.auto()
    RIGHT_TO_LEFT = enum.auto()

    def opposite(self) -> "Direction":
        if self is Direction.LEFT_TO_RIGHT:
            return Direction.RIGHT_TO_LEFT
        else:
            return Direction.LEFT_TO_RIGHT


class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        def next_level_nodes_in_reversed_order(
            nodes: list[TreeNode | None], direction: Direction
        ) -> TreeNode | None:
            for node in reversed(nodes):
                if node is None:
                    continue
                match direction:
                    case Direction.LEFT_TO_RIGHT:
                        yield node.left
                        yield node.right
                    case Direction.RIGHT_TO_LEFT:
                        yield node.right
                        yield node.left

        node_vals_by_level = []
        direction = Direction.RIGHT_TO_LEFT
        nodes = [root]
        while nodes:
            node_vals = [node.val for node in nodes if node is not None]
            if not node_vals:
                break
            node_vals_by_level.append(node_vals)

            next_nodes = []
            for node in next_level_nodes_in_reversed_order(nodes, direction):
                next_nodes.append(node)
            nodes = next_nodes
            direction = direction.opposite()

        return node_vals_by_level
