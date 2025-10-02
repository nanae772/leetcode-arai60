class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        stack = [(root, 0)]
        while stack:
            node, sum_ = stack.pop()
            sum_ += node.val
            if is_leaf(node) and sum_ == targetSum:
                return True

            if node.left is not None:
                stack.append((node.left, sum_))
            if node.right is not None:
                stack.append((node.right, sum_))

        return False


def is_leaf(node: TreeNode) -> bool:
    return node.left is None and node.right is None
