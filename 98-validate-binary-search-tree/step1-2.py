from collections.abc import Callable


def is_leaf(node: TreeNode) -> bool:
    return node.left is None and node.right is None


class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        def get_func_value_in_subtree(
            root: TreeNode, func: Callable[[int, int], int]
        ) -> int:
            if is_leaf(root):
                return root.val

            result = root.val
            if root.left is not None:
                result = func(result, get_func_value_in_subtree(root.left, func))
            if root.right is not None:
                result = func(result, get_func_value_in_subtree(root.right, func))

            return result

        def is_valid_bst(root: TreeNode) -> bool:
            if is_leaf(root):
                return True

            if root.left is not None:
                if not is_valid_bst(root.left):
                    return False

                max_left_subtree = get_func_value_in_subtree(root.left, max)
                if max_left_subtree >= root.val:
                    return False

            if root.right is not None:
                if not is_valid_bst(root.right):
                    return False

                min_right_subtree = get_func_value_in_subtree(root.right, min)
                if min_right_subtree <= root.val:
                    return False

            return True

        if root is None:
            return False
        return is_valid_bst(root)
