class Solution:
    def minDepth(self, root: TreeNode | None) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1

        min_depth = float("inf")
        if root.left is not None:
            min_depth = min(min_depth, self.minDepth(root.left) + 1)
        if root.right is not None:
            min_depth = min(min_depth, self.minDepth(root.right) + 1)
        return min_depth
