"""
Problem: Binary Tree Zigzag Level Order Traversal
Return node values level by level, alternating direction: the first
level is read left to right, the next right to left, and so on.
Example: [3,9,20,null,null,15,7] -> [[3],[20,9],[15,7]]

Approach: Breadth-first search with a queue, processing exactly the
nodes currently in the queue as one level before moving to the next.
A level flag records which direction the level is read in: values are
collected left to right as dequeued and reversed on the levels that
read right to left, so the traversal order of the queue itself never
changes and children are always enqueued left before right.

Time Complexity: O(n)
Space Complexity: O(n)
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass, field


@dataclass
class TreeNode:
    val: int
    left: TreeNode | None = field(default=None)
    right: TreeNode | None = field(default=None)


def zigzag_level_order(root: TreeNode | None) -> list[list[int]]:
    """Return the zigzag level-order traversal of a binary tree."""
    if root is None:
        return []
    result: list[list[int]] = []
    queue: deque[TreeNode] = deque([root])
    left_to_right = True
    while queue:
        level: list[int] = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        if not left_to_right:
            level.reverse()
        result.append(level)
        left_to_right = not left_to_right
    return result


if __name__ == "__main__":
    tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert zigzag_level_order(tree) == [[3], [20, 9], [15, 7]]
    # Deeper tree: direction alternates on every level
    deep = TreeNode(
        1,
        TreeNode(2, TreeNode(4), TreeNode(5)),
        TreeNode(3, TreeNode(6), TreeNode(7)),
    )
    assert zigzag_level_order(deep) == [[1], [3, 2], [4, 5, 6, 7]]
    # A left-only chain reads one value per level, direction irrelevant
    chain = TreeNode(1, TreeNode(2, TreeNode(3)))
    assert zigzag_level_order(chain) == [[1], [2], [3]]
    # Edge cases: empty tree, single node
    assert zigzag_level_order(None) == []
    assert zigzag_level_order(TreeNode(42)) == [[42]]
    print("binary_tree_zigzag_level_order_traversal: OK")
