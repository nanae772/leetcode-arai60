class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if root is None:
            return []

        node_vals_by_level = []
        nodes = [root]
        while nodes:
            node_vals_by_level.append([node.val for node in nodes])
            next_nodes = [
                node
                for node in itertools.chain(
                    *([node.left, node.right] for node in nodes)
                )
                if node is not None
            ]
            nodes = next_nodes

        return node_vals_by_level
