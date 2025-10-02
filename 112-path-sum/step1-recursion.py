class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def is_leaf(node: TreeNode) -> bool:
            return node.left is None and node.right is None

        def has_path_sum(node: TreeNode | None, target: int) -> bool:
            if node is None:
                return False
            if is_leaf(node):
                return target == node.val

            new_target = target - node.val
            return has_path_sum(node.left, new_target) or has_path_sum(
                node.right, new_target
            )

        return has_path_sum(root, targetSum)
