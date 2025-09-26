class Solution:
    def minDepth(self, root: TreeNode | None) -> int:
        if root is None:
            return 0

        def is_leaf(node: TreeNode) -> bool:
            return node.left is None and node.right is None

        nodes = deque([(root, 1)])
        while nodes:
            node, depth = nodes.popleft()
            if is_leaf(node):
                return depth
            if node.left is not None:
                nodes.append((node.left, depth + 1))
            if node.right is not None:
                nodes.append((node.right, depth + 1))
