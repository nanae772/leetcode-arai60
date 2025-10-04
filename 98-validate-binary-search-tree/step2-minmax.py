import functools
import sys
import time
from collections.abc import Callable

sys.setrecursionlimit(2 * 10**5)


def is_leaf(node: TreeNode) -> bool:
    return node.left is None and node.right is None


class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        def is_bst_with_range(root: TreeNode) -> tuple[bool, int, int]:
            if is_leaf(root):
                return True, root.val, root.val

            is_valid = True
            min_val = root.val
            max_val = root.val
            if root.left is not None:
                is_valid_left, min_left, max_left = is_bst_with_range(root.left)
                is_valid &= is_valid_left and (max_left < root.val)
                min_val = min(min_val, min_left)
                max_val = max(max_val, max_left)

            if root.right is not None:
                is_valid_right, min_right, max_right = is_bst_with_range(root.right)
                is_valid &= is_valid_right and (root.val < min_right)
                min_val = min(min_val, min_right)
                max_val = max(max_val, max_right)

            return is_valid, min_val, max_val

        if root is None:
            return False

        is_bst, _, _ = is_bst_with_range(root)
        return is_bst


# 以下は実行時間測定用に書いたコードなので読まなくても大丈夫です


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Convert Sorted Array to Binary Search Tree から流用
def sortedArrayToBST(nums: list[int]) -> TreeNode | None:
    def convert_to_height_balanced_tree(begin: int, end: int) -> TreeNode | None:
        if begin == end:
            return None
        mid = (begin + end) // 2
        root = TreeNode(nums[mid])
        root.left = convert_to_height_balanced_tree(begin, mid)
        root.right = convert_to_height_balanced_tree(mid + 1, end)
        return root

    return convert_to_height_balanced_tree(0, len(nums))


if __name__ == "__main__":
    NUMBER_OF_NODE = 10**4
    # 木が偏って一直線になるケース
    # root = TreeNode(0)
    # node = root
    # for i in range(1, NUMBER_OF_NODE):
    #     node.right = TreeNode(i)
    #     node = node.right

    # height-balanced treeのケース
    root = sortedArrayToBST(list(range(NUMBER_OF_NODE)))

    solver = Solution()
    t0 = time.perf_counter()
    ok = solver.isValidBST(root)
    t1 = time.perf_counter()

    print("isValidBST returned:", ok)
    print(f"wall-clock elapsed: {(t1 - t0):.6f} seconds")
