class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def is_leaf(node: TreeNode) -> bool:
            return node.left is None and node.right is None

        if root is None:
            return False

        stack = [(root, 0)]
        while stack:
            node, path_sum = stack.pop()
            path_sum += node.val
            if is_leaf(node) and path_sum == targetSum:
                return True

            if node.left is not None:
                stack.append((node.left, path_sum))
            if node.right is not None:
                stack.append((node.right, path_sum))
        return False
