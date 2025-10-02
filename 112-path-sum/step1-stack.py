class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def is_leaf(node: TreeNode) -> bool:
            return node.left is None and node.right is None

        stack = [(root, 0)]
        while stack:
            node, path_sum = stack.pop()
            if node is None:
                continue

            path_sum += node.val
            if is_leaf(node) and path_sum == targetSum:
                return True
            stack.append((node.left, path_sum))
            stack.append((node.right, path_sum))

        return False
