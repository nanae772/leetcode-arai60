class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        def convert_to_height_balanced_tree(begin: int, end: int) -> TreeNode | None:
            if begin == end:
                return None
            mid = (begin + end) // 2
            root = TreeNode(nums[mid])
            root.left = convert_to_height_balanced_tree(begin, mid)
            root.right = convert_to_height_balanced_tree(mid + 1, end)
            return root

        return convert_to_height_balanced_tree(0, len(nums))
