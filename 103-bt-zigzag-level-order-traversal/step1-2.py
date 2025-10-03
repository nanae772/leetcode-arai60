class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if root is None:
            return []

        node_vals_by_level = []
        nodes = [root]
        is_reverse = False
        while nodes:
            nodes_append = nodes
            if is_reverse:
                nodes_append = reversed(nodes)
            node_vals_by_level.append([node.val for node in nodes_append])

            next_nodes = []
            for node in nodes:
                if node.left is not None:
                    next_nodes.append(node.left)
                if node.right is not None:
                    next_nodes.append(node.right)

            nodes = next_nodes
            is_reverse ^= True

        return node_vals_by_level
