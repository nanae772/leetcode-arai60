import enum


class ChildDirection(enum.Enum):
    LEFT = enum.auto()
    RIGHT = enum.auto()


# top-down + 再帰関数


class Solution:
    def mergeTrees(
        self, root1: TreeNode | None, root2: TreeNode | None
    ) -> TreeNode | None:
        def get_left(node: TreeNode | None) -> TreeNode | None:
            return node.left if node is not None else None

        def get_right(node: TreeNode | None) -> TreeNode | None:
            return node.right if node is not None else None

        def merge_trees_helper(
            node1: TreeNode | None,
            node2: TreeNode | None,
            parent: TreeNode | None,
            child_direction: ChildDirection | None,
        ) -> TreeNode | None:
            if node1 is None and node2 is None:
                return None

            merged_node = TreeNode(0)
            if parent is not None:
                match child_direction:
                    case ChildDirection.LEFT:
                        parent.left = merged_node
                    case ChildDirection.RIGHT:
                        parent.right = merged_node

            if node1 is not None:
                merged_node.val += node1.val
            if node2 is not None:
                merged_node.val += node2.val
            merge_trees_helper(
                get_left(node1), get_left(node2), merged_node, ChildDirection.LEFT
            )
            merge_trees_helper(
                get_right(node1), get_right(node2), merged_node, ChildDirection.RIGHT
            )
            return merged_node

        return merge_trees_helper(root1, root2, None, None)
