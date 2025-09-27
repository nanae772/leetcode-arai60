# bottom-up + 再帰関数
class Solution:
    def mergeTrees(
        self, root1: TreeNode | None, root2: TreeNode | None
    ) -> TreeNode | None:
        if root1 is None and root2 is None:
            return None

        merged_node = TreeNode(0)
        if root1 is not None:
            merged_node.val += root1.val
        if root2 is not None:
            merged_node.val += root2.val

        def get_left(node: TreeNode | None) -> TreeNode | None:
            return node.left if node is not None else None

        def get_right(node: TreeNode | None) -> TreeNode | None:
            return node.right if node is not None else None

        merged_node.left = self.mergeTrees(get_left(root1), get_left(root2))
        merged_node.right = self.mergeTrees(get_right(root1), get_right(root2))
        return merged_node
