# step1-stack.pyを再帰で書いてみる解法
# 上から下へ深さを確定させていく


class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        max_depth = 0

        def update_max_depth(node: TreeNode | None, depth: int) -> None:
            if node is None:
                return
            nonlocal max_depth
            max_depth = max(max_depth, depth)
            update_max_depth(node.left, depth + 1)
            update_max_depth(node.right, depth + 1)

        update_max_depth(root, 1)
        return max_depth
