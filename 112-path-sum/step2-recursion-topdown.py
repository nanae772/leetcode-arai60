class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def is_leaf(node: TreeNode) -> bool:
            return node.left is None and node.right is None

        has_path_sum = False

        def has_path_sum_helper(node: TreeNode | None, path_sum: int):
            nonlocal has_path_sum
            if has_path_sum:  # 枝狩り(1個見つかったらそれ以上探索する必要は無い)
                return

            path_sum += node.val
            if is_leaf(node) and path_sum == targetSum:
                has_path_sum = True
                return

            if node.left is not None:
                has_path_sum_helper(node.left, path_sum)
            if node.right is not None:
                has_path_sum_helper(node.right, path_sum)

        has_path_sum_helper(root, 0)
        return has_path_sum
