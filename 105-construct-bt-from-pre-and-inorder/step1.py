class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        if not preorder or len(preorder) != len(inorder):
            return None

        val_to_inorder_index = dict()
        for i, val in enumerate(inorder):
            val_to_inorder_index[val] = i

        preorder_index = 0

        def construct_binary_tree(begin: int, end: int) -> TreeNode | None:
            if begin == end:
                return None

            nonlocal preorder_index
            root = TreeNode(preorder[preorder_index])
            preorder_index += 1
            root_val_index_inorder = val_to_inorder_index[root.val]
            root.left = construct_binary_tree(begin, root_val_index_inorder)
            root.right = construct_binary_tree(root_val_index_inorder + 1, end)
            return root

        return construct_binary_tree(0, len(preorder))
