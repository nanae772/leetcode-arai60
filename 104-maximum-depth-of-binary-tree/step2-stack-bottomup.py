from dataclasses import dataclass
from typing import Optional


@dataclass
class NodeWithHeight:
    node: TreeNode | None
    parent: Optional["NodeWithHeight"]  # "NodeWithHeight" | None と書けない
    height: int = -1


# step1-recursion.pyの再帰をなるべく再現しようとしたスタック解法
# 下から上へ高さを確定させていく


class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        def is_leaf(node: TreeNode) -> bool:
            return node.left is None and node.right is None

        if root is None:
            return 0

        nodes_with_height = [NodeWithHeight(root, None, -1)]
        while nodes_with_height:
            node_with_height = nodes_with_height[-1]
            if node_with_height.height != -1:
                if node_with_height.parent is None:  # root
                    return node_with_height.height
                node_with_height.parent.height = max(
                    node_with_height.parent.height, node_with_height.height + 1
                )
                nodes_with_height.pop()
                continue
            if is_leaf(node_with_height.node):
                node_with_height.height = 1
                continue

            left = node_with_height.node.left
            right = node_with_height.node.right
            if left is not None:
                nodes_with_height.append(NodeWithHeight(left, node_with_height, -1))
            if right is not None:
                nodes_with_height.append(NodeWithHeight(right, node_with_height, -1))
