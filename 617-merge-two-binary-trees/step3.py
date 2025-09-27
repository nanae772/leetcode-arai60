import enum


class Side(enum.Enum):
    LEFT = enum.auto()
    RIGHT = enum.auto()


class Solution:
    def mergeTrees(
        self, root1: TreeNode | None, root2: TreeNode | None
    ) -> TreeNode | None:
        def get_child(node: TreeNode | None, side: Side) -> TreeNode | None:
            if node is None:
                return None
            match side:
                case Side.LEFT:
                    return node.left
                case Side.RIGHT:
                    return node.right

        dummy = TreeNode()
        stack = [(root1, root2, dummy, Side.LEFT)]
        while stack:
            node1, node2, parent, side = stack.pop()
            if node1 is None and node2 is None:
                continue

            merged_node = TreeNode(0)
            if node1 is not None:
                merged_node.val += node1.val
            if node2 is not None:
                merged_node.val += node2.val
            match side:
                case Side.LEFT:
                    parent.left = merged_node
                case Side.RIGHT:
                    parent.right = merged_node

            for next_side in Side:
                stack.append(
                    (
                        get_child(node1, next_side),
                        get_child(node2, next_side),
                        merged_node,
                        next_side,
                    )
                )

        return dummy.left
