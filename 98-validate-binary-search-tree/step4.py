class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        if root is None:
            return False

        def get_val_in_order(root: TreeNode) -> int:
            if root.left is not None:
                yield from get_val_in_order(root.left)
            yield root.val
            if root.right is not None:
                yield from get_val_in_order(root.right)

        return all(a < b for a, b in itertools.pairwise(get_val_in_order(root)))
