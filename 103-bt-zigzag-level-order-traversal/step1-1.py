class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if root is None:
            return []

        node_vals_by_level = []
        is_reverse = True
        nodes = [root]
        while nodes:
            node_vals_by_level.append([node.val for node in nodes])
            next_nodes = []
            for node in reversed(nodes):
                if is_reverse:
                    if node.right is not None:
                        next_nodes.append(node.right)
                    if node.left is not None:
                        next_nodes.append(node.left)
                else:
                    if node.left is not None:
                        next_nodes.append(node.left)
                    if node.right is not None:
                        next_nodes.append(node.right)

            nodes = next_nodes
            is_reverse ^= True

        return node_vals_by_level
