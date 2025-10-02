class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        node_vals_by_level = []

        def build_node_vals_by_level(node: TreeNode, depth: int) -> None:
            if node is None:
                return
            while depth >= len(node_vals_by_level):
                node_vals_by_level.append([])

            node_vals_by_level[depth].append(node.val)
            build_node_vals_by_level(node.left, depth + 1)
            build_node_vals_by_level(node.right, depth + 1)

        build_node_vals_by_level(root, 0)
        return node_vals_by_level
