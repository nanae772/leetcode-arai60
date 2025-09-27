import enum


class ChildDirection(enum.Enum):
    LEFT = enum.auto()
    RIGHT = enum.auto()


# top-down + stack


class Solution:
    def mergeTrees(
        self, root1: TreeNode | None, root2: TreeNode | None
    ) -> TreeNode | None:
        def get_left(node: TreeNode | None) -> TreeNode | None:
            return node.left if node is not None else None

        def get_right(node: TreeNode | None) -> TreeNode | None:
            return node.right if node is not None else None

        stack = [(root1, root2, None, None)]
        merged_root = None

        while stack:
            node1, node2, parent, child_direction = stack.pop()
            if node1 is None and node2 is None:
                continue

            merged_node = TreeNode(0)
            if node1 is not None:
                merged_node.val += node1.val
            if node2 is not None:
                merged_node.val += node2.val
            if parent is not None:
                match child_direction:
                    case ChildDirection.LEFT:
                        parent.left = merged_node
                    case ChildDirection.RIGHT:
                        parent.right = merged_node
            if merged_root is None:
                merged_root = merged_node

            stack.append(
                (get_left(node1), get_left(node2), merged_node, ChildDirection.LEFT)
            )
            stack.append(
                (get_right(node1), get_right(node2), merged_node, ChildDirection.RIGHT)
            )

        return merged_root
