# bottom-up + stack
class Solution:
    def mergeTrees(
        self, root1: TreeNode | None, root2: TreeNode | None
    ) -> TreeNode | None:
        def get_left(node: TreeNode | None) -> TreeNode | None:
            return node.left if node is not None else None

        def get_right(node: TreeNode | None) -> TreeNode | None:
            return node.right if node is not None else None

        merged_root = None
        stack = [(root1, root2, [], [], [])]
        while stack:
            node1, node2, result_ref, left_ref, right_ref = stack[-1]

            if node1 is None and node2 is None:
                result_ref.append(None)
                stack.pop()
                continue
            if not left_ref:
                stack.append((get_left(node1), get_left(node2), left_ref, [], []))
                continue
            if not right_ref:
                stack.append((get_right(node1), get_right(node2), right_ref, [], []))
                continue

            merged_node = TreeNode(0)
            if node1 is not None:
                merged_node.val += node1.val
            if node2 is not None:
                merged_node.val += node2.val

            merged_node.left = left_ref[0]
            merged_node.right = right_ref[0]
            result_ref.append(merged_node)
            merged_root = merged_node
            stack.pop()

        return merged_root
