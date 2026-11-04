"""
Problem: Maximum Depth of Binary Tree
Return the number of nodes along the longest root-to-leaf path.
Example: tree [3,9,20,null,null,15,7] -> 3

Approach: Recursion. The depth of a node is 1 + max(depth of its
children); an empty tree has depth 0. An iterative BFS version is also
included to show both styles.

Time Complexity: O(n)
Space Complexity: O(h) recursion stack, h = tree height
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass, field


@dataclass
class TreeNode:
    val: int
    left: TreeNode | None = field(default=None)
    right: TreeNode | None = field(default=None)


def max_depth(root: TreeNode | None) -> int:
    """Return the maximum depth of a binary tree (recursive)."""
    if root is None:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


def max_depth_bfs(root: TreeNode | None) -> int:
    """Return the maximum depth of a binary tree (level-order BFS)."""
    if root is None:
        return 0
    depth = 0
    queue: deque[TreeNode] = deque([root])
    while queue:
        depth += 1
        for _ in range(len(queue)):
            node = queue.popleft()
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
    return depth


if __name__ == "__main__":
    tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert max_depth(tree) == 3
    assert max_depth_bfs(tree) == 3
    print("maximum_depth_of_binary_tree: OK")
