"""
Problem: Construct Binary Tree from Preorder and Inorder Traversal
Given the preorder and inorder traversals of a binary tree with
distinct values, rebuild and return the tree.
Example: preorder=[3,9,20,15,7], inorder=[9,3,15,20,7] ->
[3,9,20,null,null,15,7]

Approach: The first preorder value is the root. Its position in the
inorder traversal splits the remaining values into the left subtree
(everything before it) and the right subtree (everything after it),
and the sizes of those splits say exactly how many of the following
preorder values belong to each side. A value-to-inorder-index map
makes each split O(1), so a recursive build consumes the preorder
list left to right, recursing left before right. Inconsistent inputs
raise ValueError: different lengths, different value multisets,
duplicate values (which would make the tree ambiguous), or a root
that falls outside the inorder window it is built for. Two empty
traversals build an empty tree (None).

Time Complexity: O(n)
Space Complexity: O(n)
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass, field


@dataclass
class TreeNode:
    val: int
    left: TreeNode | None = field(default=None)
    right: TreeNode | None = field(default=None)


def build_tree(preorder: list[int], inorder: list[int]) -> TreeNode | None:
    """Rebuild a binary tree from its preorder and inorder traversals.

    Raises ValueError if the traversals cannot describe one tree.
    The inputs are not mutated.
    """
    if len(preorder) != len(inorder):
        raise ValueError("preorder and inorder must have the same length")
    if Counter(preorder) != Counter(inorder):
        raise ValueError("preorder and inorder must contain the same values")
    if len(set(preorder)) != len(preorder):
        raise ValueError("values must be distinct to rebuild the tree")
    if not preorder:
        return None

    index_of = {value: i for i, value in enumerate(inorder)}
    cursor = 0

    def build(lo: int, hi: int) -> TreeNode | None:
        nonlocal cursor
        if lo > hi:
            return None
        value = preorder[cursor]
        mid = index_of[value]
        if not lo <= mid <= hi:
            raise ValueError("traversals are inconsistent")
        cursor += 1
        node = TreeNode(value)
        node.left = build(lo, mid - 1)
        node.right = build(mid + 1, hi)
        return node

    return build(0, len(inorder) - 1)


def level_order(root: TreeNode | None) -> list[int | None]:
    """Return level-order values with None placeholders, for checking."""
    if root is None:
        return []
    result: list[int | None] = []
    queue: list[TreeNode | None] = [root]
    while queue:
        node = queue.pop(0)
        if node is None:
            result.append(None)
            continue
        result.append(node.val)
        queue.append(node.left)
        queue.append(node.right)
    while result and result[-1] is None:
        result.pop()
    return result


if __name__ == "__main__":
    tree = build_tree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    assert level_order(tree) == [3, 9, 20, None, None, 15, 7]
    # Left and right chains
    assert level_order(build_tree([1, 2, 3], [3, 2, 1])) == [1, 2, None, 3]
    assert level_order(build_tree([1, 2, 3], [1, 2, 3])) == [1, None, 2, None, 3]
    # A balanced tree round-trips through both traversals
    balanced = build_tree([1, 2, 4, 5, 3, 6, 7], [4, 2, 5, 1, 6, 3, 7])
    assert level_order(balanced) == [1, 2, 3, 4, 5, 6, 7]
    # Edge cases: empty traversals, single node
    assert build_tree([], []) is None
    single = build_tree([42], [42])
    assert single is not None and single.val == 42
    assert single.left is None and single.right is None
    # Inconsistent inputs raise
    for bad_pre, bad_in in (
        ([1, 2], [1]),
        ([1, 2], [1, 3]),
        ([1, 1], [1, 1]),
        ([2, 1, 3], [3, 2, 1]),
    ):
        try:
            build_tree(bad_pre, bad_in)
        except ValueError:
            pass
        else:
            raise AssertionError(f"expected ValueError for {bad_pre}, {bad_in}")
    print("construct_binary_tree_from_preorder_and_inorder: OK")
