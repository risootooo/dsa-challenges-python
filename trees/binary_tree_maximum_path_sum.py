"""
Problem: Binary Tree Maximum Path Sum
A path in a binary tree is any sequence of nodes connected by edges where
no node repeats; it need not pass through the root. Return the maximum sum
of node values over all paths.
Example: [1,2,3] -> 6;  [-10,9,20,null,null,15,7] -> 42 (15 + 20 + 7)

Approach: One post-order DFS returns, for each node, the best downward gain:
node.val + max(0, best child gain) — negative child gains are dropped, since
a path is never obliged to include them. Separately, the best path *through*
the node (left gain + node + right gain) is a candidate for the global
answer, because the optimal path can bend at exactly one node.

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


def max_path_sum(root: TreeNode | None) -> int:
    """Return the maximum sum over all paths in the tree."""
    if root is None:
        raise ValueError("tree must be non-empty")
    best = root.val

    def gain(node: TreeNode | None) -> int:
        """Best downward path sum starting at `node` (one side only)."""
        nonlocal best
        if node is None:
            return 0
        left = max(gain(node.left), 0)
        right = max(gain(node.right), 0)
        best = max(best, node.val + left + right)  # path bending at node
        return node.val + max(left, right)

    gain(root)
    return best


if __name__ == "__main__":
    assert max_path_sum(TreeNode(1, TreeNode(2), TreeNode(3))) == 6
    tree = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert max_path_sum(tree) == 42
    assert max_path_sum(TreeNode(-3)) == -3
    print("binary_tree_maximum_path_sum: OK")
