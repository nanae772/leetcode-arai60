class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        if root is None:
            return False

        stack = [(root, -float("inf"), float("inf"))]
        while stack:
            node, lower_bound, upper_bound = stack.pop()
            if not (lower_bound < node.val < upper_bound):
                return False

            if node.left is not None:
                stack.append((node.left, lower_bound, min(upper_bound, node.val)))
            if node.right is not None:
                stack.append((node.right, max(lower_bound, node.val), upper_bound))

        return True
