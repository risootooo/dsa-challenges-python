"""
Problem: Kth Smallest Element in a BST
Given the root of a binary search tree and an integer k, return the
kth smallest value (1-indexed) among all the values of the nodes in
the tree.
Example: tree [3,1,4,null,2] with k=1 -> 1; tree
[5,3,6,2,4,null,null,1] with k=3 -> 3

Approach: Iterative inorder traversal with an explicit stack. An
inorder walk of a BST visits values in ascending order, so counting
visited nodes and stopping at the kth visit gives the answer without
traversing the rest of the tree. The traversal pushes the whole left
spine, pops the smallest remaining node, then moves to its right
subtree and repeats.

Time Complexity: O(h + k), h = tree height
Space Complexity: O(h) for the stack
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class TreeNode:
    val: int
    left: TreeNode | None = field(default=None)
    right: TreeNode | None = field(default=None)


def kth_smallest(root: TreeNode | None, k: int) -> int:
    """Return the kth smallest value (1-indexed) in the BST at ``root``.

    Raises ValueError if ``k`` is out of range or the tree is empty.
    """
    if root is None or k < 1:
        raise ValueError("k must be a positive 1-indexed position in a non-empty tree")
    stack: list[TreeNode] = []
    current: TreeNode | None = root
    count = 0
    while stack or current is not None:
        while current is not None:
            stack.append(current)
            current = current.left
        current = stack.pop()
        count += 1
        if count == k:
            return current.val
        current = current.right
    raise ValueError("k exceeds the number of nodes in the tree")


if __name__ == "__main__":
    tree = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
    assert kth_smallest(tree, 1) == 1
    assert kth_smallest(tree, 2) == 2
    assert kth_smallest(tree, 4) == 4
    larger = TreeNode(
        5,
        TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)),
        TreeNode(6),
    )
    assert kth_smallest(larger, 3) == 3
    assert kth_smallest(larger, 6) == 6
    # Edge cases: single node, left spine only
    assert kth_smallest(TreeNode(1), 1) == 1
    spine = TreeNode(3, TreeNode(2, TreeNode(1)))
    assert kth_smallest(spine, 3) == 3
    # Out-of-range k raises instead of returning a wrong value
    for bad_root, bad_k in ((None, 1), (tree, 0), (tree, 5)):
        try:
            kth_smallest(bad_root, bad_k)  # type: ignore[arg-type]
        except ValueError:
            pass
        else:
            raise AssertionError("expected ValueError")
    print("kth_smallest_in_bst: OK")
