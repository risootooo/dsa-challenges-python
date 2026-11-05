"""
Problem: Validate Binary Search Tree
Determine whether a binary tree is a valid binary search tree: for
every node, all values in its left subtree are strictly smaller and
all values in its right subtree are strictly larger.
Example: tree [2,1,3] -> True; tree [5,1,4,null,null,3,6] -> False

Approach: Recursion with an allowed (low, high) value range. The root
may hold any value; each left child inherits the parent's value as its
upper bound and each right child inherits it as its lower bound, so a
node that looks fine against its parent but violates an ancestor's
bound is still rejected. Checking only parent/child pairs is not
sufficient.

Time Complexity: O(n)
Space Complexity: O(h) recursion stack, h = tree height
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class TreeNode:
    val: int
    left: TreeNode | None = field(default=None)
    right: TreeNode | None = field(default=None)


def is_valid_bst(root: TreeNode | None) -> bool:
    """Return True if ``root`` is a valid binary search tree."""

    def check(node: TreeNode | None, low: float, high: float) -> bool:
        if node is None:
            return True
        if not (low < node.val < high):
            return False
        return check(node.left, low, node.val) and check(
            node.right, node.val, high
        )

    return check(root, float("-inf"), float("inf"))


if __name__ == "__main__":
    assert is_valid_bst(TreeNode(2, TreeNode(1), TreeNode(3))) is True
    invalid = TreeNode(
        5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6))
    )
    assert is_valid_bst(invalid) is False
    assert is_valid_bst(None) is True
    assert is_valid_bst(TreeNode(1)) is True
    print("validate_binary_search_tree: OK")
