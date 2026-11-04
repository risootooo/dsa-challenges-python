"""
Problem: Invert Binary Tree
Swap the left and right children of every node in a binary tree.
Example: [4,2,7,1,3,6,9] -> [4,7,2,9,6,3,1]

Approach: Depth-first recursion: invert both subtrees, then swap them
at the current node.

Time Complexity: O(n)
Space Complexity: O(h) recursion stack
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class TreeNode:
    val: int
    left: TreeNode | None = field(default=None)
    right: TreeNode | None = field(default=None)


def invert_tree(root: TreeNode | None) -> TreeNode | None:
    """Invert a binary tree in place and return its root."""
    if root is None:
        return None
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root


if __name__ == "__main__":
    tree = TreeNode(2, TreeNode(1), TreeNode(3))
    inverted = invert_tree(tree)
    assert inverted is not None and inverted.left is not None and inverted.right is not None
    assert (inverted.left.val, inverted.right.val) == (3, 1)
    print("invert_binary_tree: OK")
