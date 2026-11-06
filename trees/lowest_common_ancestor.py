"""
Problem: Lowest Common Ancestor of a Binary Tree
Given a binary tree and two nodes p and q in it, return their lowest
common ancestor: the deepest node that has both p and q as descendants
(a node may be its own descendant).
Example: tree [3,5,1,6,2,0,8,null,null,7,4], p=5, q=1 -> 3;
p=5, q=4 -> 5

Approach: Recursive DFS. If the current node is None, p, or q, return
it. Otherwise search both subtrees: if p and q are found in different
subtrees, the current node is their split point and therefore the
LCA; if only one side reports a hit, propagate that hit upward. This
relies on both nodes being present in the tree.

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


def lowest_common_ancestor(
    root: TreeNode | None, p: TreeNode | None, q: TreeNode | None
) -> TreeNode | None:
    """Return the lowest common ancestor of ``p`` and ``q`` in ``root``."""
    if root is None or root is p or root is q:
        return root
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    if left is not None and right is not None:
        return root
    return left if left is not None else right


if __name__ == "__main__":
    # [3,5,1,6,2,0,8,null,null,7,4]
    n7, n4 = TreeNode(7), TreeNode(4)
    n6, n2 = TreeNode(6), TreeNode(2, n7, n4)
    n5, n1 = TreeNode(5, n6, n2), TreeNode(1, TreeNode(0), TreeNode(8))
    root = TreeNode(3, n5, n1)
    assert lowest_common_ancestor(root, n5, n1) is root
    assert lowest_common_ancestor(root, n5, n4) is n5
    assert lowest_common_ancestor(root, n7, n4) is n2
    assert lowest_common_ancestor(root, n6, n4) is n5
    assert lowest_common_ancestor(root, root, n4) is root
    assert lowest_common_ancestor(None, n5, n1) is None
    assert lowest_common_ancestor(root, n5, n5) is n5
    print("lowest_common_ancestor: OK")
