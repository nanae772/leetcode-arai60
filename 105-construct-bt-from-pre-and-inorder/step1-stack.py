class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        if not preorder or len(preorder) != len(inorder):
            return None

        val_to_inorder_index = dict()
        for i, val in enumerate(inorder):
            val_to_inorder_index[val] = i

        preorder_index = 0
        root = None
        stack = [(0, len(preorder), None, False)]
        while stack:
            begin, end, parent, is_left = stack.pop()
            if begin == end:
                continue

            node = TreeNode(preorder[preorder_index])
            preorder_index += 1
            if parent is not None:
                if is_left:
                    parent.left = node
                else:
                    parent.right = node

            node_val_index_inorder = val_to_inorder_index[node.val]
            stack.append((node_val_index_inorder + 1, end, node, False))
            stack.append((begin, node_val_index_inorder, node, True))

            if root is None:
                root = node

        return root
