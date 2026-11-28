"""
Problem: Subtree of Another Tree
Given the roots of two binary trees root and subRoot, return True if
there is a subtree of root with the same structure and node values as
subRoot, and False otherwise. A subtree of a binary tree is a tree
consisting of a node of the original tree and all of its descendants.
Example: root [3,4,5,1,2], subRoot [4,1,2] -> True; root
[3,4,5,1,2,null,null,null,null,0], subRoot [4,1,2] -> False (the 2 in
root has an extra left child 0, so the structures differ)

Approach: Depth-first search over root. At every node, run an exact
same-tree comparison against subRoot (both trees walked together,
values and shape must match at every step). If any node matches, the
answer is True; if the search exhausts root without a match, it is
False. The exact comparison is what rejects near-misses where subRoot
appears as a prefix of a larger subtree.

Time Complexity: O(n * m) worst case, n = nodes in root, m = nodes in
subRoot
Space Complexity: O(h) recursion stack, h = height of root
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class TreeNode:
    val: int
    left: TreeNode | None = field(default=None)
    right: TreeNode | None = field(default=None)


def _is_same_tree(p: TreeNode | None, q: TreeNode | None) -> bool:
    """Return True iff trees ``p`` and ``q`` are structurally identical
    with equal values at every node."""
    if p is None or q is None:
        return p is q
    return (
        p.val == q.val
        and _is_same_tree(p.left, q.left)
        and _is_same_tree(p.right, q.right)
    )


def is_subtree(root: TreeNode | None, sub_root: TreeNode | None) -> bool:
    """Return True iff some subtree of ``root`` exactly equals
    ``sub_root`` in structure and values.

    An empty ``sub_root`` is a subtree of any tree (including an empty
    one); a non-empty ``sub_root`` is never a subtree of an empty tree.
    """
    if sub_root is None:
        return True
    if root is None:
        return False
    return (
        _is_same_tree(root, sub_root)
        or is_subtree(root.left, sub_root)
        or is_subtree(root.right, sub_root)
    )


if __name__ == "__main__":
    # root [3,4,5,1,2], subRoot [4,1,2] -> True
    root = TreeNode(
        3,
        TreeNode(4, TreeNode(1), TreeNode(2)),
        TreeNode(5),
    )
    sub = TreeNode(4, TreeNode(1), TreeNode(2))
    assert is_subtree(root, sub) is True
    # Same values, but root's 2 has an extra left child 0 -> False
    root_extra = TreeNode(
        3,
        TreeNode(4, TreeNode(1), TreeNode(2, TreeNode(0))),
        TreeNode(5),
    )
    assert is_subtree(root_extra, sub) is False
    # The whole tree is a subtree of itself
    assert is_subtree(root, root) is True
    # Match deep in the right subtree
    deep = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4, TreeNode(5))))
    assert is_subtree(deep, TreeNode(4, TreeNode(5))) is True
    assert is_subtree(deep, TreeNode(4, None, TreeNode(5))) is False
    # Edge cases: empty trees, single nodes
    assert is_subtree(None, None) is True
    assert is_subtree(TreeNode(1), None) is True
    assert is_subtree(None, TreeNode(1)) is False
    assert is_subtree(TreeNode(1), TreeNode(1)) is True
    assert is_subtree(TreeNode(1), TreeNode(2)) is False
    print("subtree_of_another_tree: OK")
