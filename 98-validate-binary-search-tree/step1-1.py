def is_leaf(node: TreeNode) -> bool:
    return node.left is None and node.right is None


class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        def get_max_in_subtree(root: TreeNode) -> int:
            if is_leaf(root):
                return root.val

            max_val = root.val
            if root.left is not None:
                max_val = max(max_val, get_max_in_subtree(root.left))
            if root.right is not None:
                max_val = max(max_val, get_max_in_subtree(root.right))

            return max_val

        def get_min_in_subtree(root: TreeNode) -> int:
            if is_leaf(root):
                return root.val

            min_val = root.val
            if root.left is not None:
                min_val = min(min_val, get_min_in_subtree(root.left))
            if root.right is not None:
                min_val = min(min_val, get_min_in_subtree(root.right))

            return min_val

        def is_valid_bst(root: TreeNode) -> bool:
            if is_leaf(root):
                return True

            max_left_subtree = -float("inf")
            min_right_subtree = float("inf")
            if root.left is not None:
                if not is_valid_bst(root.left):
                    return False
                max_left_subtree = get_max_in_subtree(root.left)
            if root.right is not None:
                if not is_valid_bst(root.right):
                    return False
                min_right_subtree = get_min_in_subtree(root.right)

            return max_left_subtree < root.val < min_right_subtree

        if root is None:
            return False
        return is_valid_bst(root)
