class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if root is None:
            return []

        node_vals_by_level = []
        nodes = [root]
        is_left_to_right = False
        while nodes:
            node_vals_by_level.append([node.val for node in nodes])

            next_nodes = []
            for node in reversed(nodes):
                if is_left_to_right:
                    next_nodes.append(node.left)
                    next_nodes.append(node.right)
                else:
                    next_nodes.append(node.right)
                    next_nodes.append(node.left)

            nodes = [node for node in next_nodes if node is not None]
            is_left_to_right = not is_left_to_right

        return node_vals_by_level
