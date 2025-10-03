# deque を使う解法
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        node_vals_by_level = []
        node_level_pairs = deque([(root, 0)])
        while node_level_pairs:
            node, level = node_level_pairs.popleft()
            if node is None:
                continue

            while level >= len(node_vals_by_level):
                node_vals_by_level.append(deque())
            if level % 2 == 0:
                node_vals_by_level[level].append(node.val)
            else:
                node_vals_by_level[level].appendleft(node.val)

            node_level_pairs.append((node.left, level + 1))
            node_level_pairs.append((node.right, level + 1))

        return [list(node_vals) for node_vals in node_vals_by_level]
