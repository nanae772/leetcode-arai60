class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        nodes_by_level = []

        def build_level_order_traversal(node: TreeNode, depth: int) -> None:
            if node is None:
                return
            if depth >= len(nodes_by_level):
                nodes_by_level.append([])

            nodes_by_level[depth].append(node.val)
            build_level_order_traversal(node.left, depth + 1)
            build_level_order_traversal(node.right, depth + 1)

        build_level_order_traversal(root, 0)
        return nodes_by_level
