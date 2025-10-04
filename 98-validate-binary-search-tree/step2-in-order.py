class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        def get_val_in_order(root: TreeNode) -> int:
            if root.left is not None:
                yield from get_val_in_order(root.left)
            yield root.val
            if root.right is not None:
                yield from get_val_in_order(root.right)

        if root is None:
            return False

        val = -float("inf")
        for next_val in get_val_in_order(root):
            if not val < next_val:
                return False
            val = next_val
        return True
