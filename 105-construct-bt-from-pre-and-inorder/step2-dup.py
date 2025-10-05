# preorder, inorder内に重複した値があっても動くバージョン
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        if len(preorder) != len(inorder):
            return None  # 例外を発生させるべきだと思うが簡易的にNoneを返すことにする

        val_to_count = collections.defaultdict(int)
        val_count_pair_to_inorder_index = dict()
        for i, val in enumerate(inorder):
            val_to_count[val] += 1
            val_count_pair_to_inorder_index[(val, val_to_count[val])] = i

        val_to_count.clear()

        def construct_binary_tree(
            begin: int, end: int, root_preorder_index: int
        ) -> TreeNode | None:
            if not begin < end:
                return None

            val = preorder[root_preorder_index]
            val_to_count[val] += 1
            root = TreeNode(val)
            root_inorder_index = val_count_pair_to_inorder_index[
                (val, val_to_count[val])
            ]
            number_nodes_left_subtree = root_inorder_index - begin
            root_left_preorder_index = root_preorder_index + 1
            root_right_preorder_index = (
                root_preorder_index + number_nodes_left_subtree + 1
            )

            root.left = construct_binary_tree(
                begin, root_inorder_index, root_left_preorder_index
            )
            root.right = construct_binary_tree(
                root_inorder_index + 1, end, root_right_preorder_index
            )
            return root

        return construct_binary_tree(0, len(inorder), 0)


if __name__ == "__main__":
    solver = Solution()
    preorder = [1, 1, 2]
    inorder = [1, 1, 2]

    root = solver.buildTree(preorder, inorder)

    # 上記のアルゴリズムでは以下の二分木が構築される
    # 1
    #  \
    #   1
    #    \
    #     2
    assert root.val == 1
    assert root.right.val == 1
    assert root.right.right.val == 2
