# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        max_depth = 0
        nodes = [(root, 0)]
        while nodes:
            node, depth = nodes.pop()
            max_depth = max(max_depth, depth)
            if node is None:
                continue
            nodes.append((node.left, depth + 1))
            nodes.append((node.right, depth + 1))
        return max_depth
