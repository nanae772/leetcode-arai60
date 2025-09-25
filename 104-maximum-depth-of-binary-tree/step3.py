class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        nodes = [(root, 0)]
        max_depth = 0
        while nodes:
            node, depth = nodes.pop()
            max_depth = max(max_depth, depth)
            if node is None:
                continue
            nodes.append((node.left, depth + 1))
            nodes.append((node.right, depth + 1))
        return max_depth
