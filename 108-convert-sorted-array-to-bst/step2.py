# sliceを渡す解法
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        def convert_to_height_balanced_tree(nums: list[int]) -> TreeNode | None:
            if not nums:
                return None
            mid = len(nums) // 2
            root = TreeNode(nums[mid])
            root.left = convert_to_height_balanced_tree(nums[:mid])
            root.right = convert_to_height_balanced_tree(nums[mid + 1 :])
            return root

        return convert_to_height_balanced_tree(nums)
