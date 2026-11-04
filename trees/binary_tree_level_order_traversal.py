"""
Problem: Binary Tree Level Order Traversal
Return node values level by level, left to right.
Example: [3,9,20,null,null,15,7] -> [[3],[9,20],[15,7]]

Approach: Breadth-first search with a queue. Process exactly the nodes
currently in the queue as one level before moving to the next.

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


def level_order(root: TreeNode | None) -> list[list[int]]:
    """Return level-order traversal of a binary tree."""
    if root is None:
        return []
    result: list[list[int]] = []
    queue: deque[TreeNode] = deque([root])
    while queue:
        level: list[int] = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        result.append(level)
    return result


if __name__ == "__main__":
    tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert level_order(tree) == [[3], [9, 20], [15, 7]]
    print("binary_tree_level_order_traversal: OK")
