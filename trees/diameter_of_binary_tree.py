"""
Problem: Diameter of Binary Tree
Given the root of a binary tree, return the length of its diameter: the
number of edges on the longest path between any two nodes. The path may
or may not pass through the root.
Example: [1,2,3,4,5] -> 3 (path 4-2-1-3 or 5-2-1-3); [1,2] -> 1

Approach: Post-order depth-first search. For each node, the longest
path passing through it joins the heights of its left and right
subtrees, so the diameter candidate at that node is left_height +
right_height (heights measured in edges, with an empty subtree at -1
so a leaf contributes 0). Track the best candidate seen anywhere while
each call returns 1 + max(child heights) to its parent. One traversal
visits every node exactly once.

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


def diameter_of_binary_tree(root: TreeNode | None) -> int:
    """Return the diameter (in edges) of a binary tree."""
    best = 0

    def height(node: TreeNode | None) -> int:
        nonlocal best
        if node is None:
            return -1
        left_h = height(node.left)
        right_h = height(node.right)
        best = max(best, left_h + right_h + 2)
        return 1 + max(left_h, right_h)

    height(root)
    return best


if __name__ == "__main__":
    tree = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    assert diameter_of_binary_tree(tree) == 3
    assert diameter_of_binary_tree(TreeNode(1, TreeNode(2))) == 1
    # Longest path does not pass through the root
    skewed = TreeNode(
        1,
        TreeNode(2, TreeNode(3, TreeNode(4, TreeNode(5))), TreeNode(6)),
    )
    assert diameter_of_binary_tree(skewed) == 4
    # Edge cases: empty tree, single node, straight chain
    assert diameter_of_binary_tree(None) == 0
    assert diameter_of_binary_tree(TreeNode(1)) == 0
    chain = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))))
    assert diameter_of_binary_tree(chain) == 3
    print("diameter_of_binary_tree: OK")
