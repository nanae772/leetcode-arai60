class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        if len(preorder) != len(inorder):
            return None

        val_to_inorder_index = {val: i for i, val in enumerate(inorder)}

        def construct_binary_tree(
            root_preorder_index: int, begin: int, end: int
        ) -> TreeNode | None:
            if not begin < end:
                return None

            root = TreeNode(preorder[root_preorder_index])
            root_inorder_index = val_to_inorder_index[root.val]
            number_nodes_left_subtree = root_inorder_index - begin

            root_left_preorder_index = root_preorder_index + 1
            root_right_preorder_index = (
                root_preorder_index + number_nodes_left_subtree + 1
            )

            root.left = construct_binary_tree(
                root_left_preorder_index,
                begin,
                root_inorder_index,
            )
            root.right = construct_binary_tree(
                root_right_preorder_index,
                root_inorder_index + 1,
                end,
            )
            return root

        return construct_binary_tree(0, 0, len(inorder))
