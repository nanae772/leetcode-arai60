class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if root is None:
            return []

        node_vals_by_level = []
        nodes = [root]
        while nodes:
            node_vals_by_level.append([node.val for node in nodes])
            next_nodes = []
            for node in nodes:
                if node.left is not None:
                    next_nodes.append(node.left)
                if node.right is not None:
                    next_nodes.append(node.right)
            nodes = next_nodes

        return node_vals_by_level
