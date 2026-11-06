"""
Problem: Binary Tree Right Side View
Given the root of a binary tree, imagine standing on its right side and
return the values of the nodes you can see, ordered top to bottom — that
is, the last node of each level in a level-order traversal.
Example: [1,2,3,null,5,null,4] -> [1,3,4]; [1,null,3] -> [1,3]

Approach: Breadth-first search with a queue. Process exactly the nodes
currently in the queue as one level; the final node dequeued in that
level is the one visible from the right, so append its value before
moving to the next level. A depth-first variant that visits the right
child first and records the first node seen at each depth is equivalent.

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


def right_side_view(root: TreeNode | None) -> list[int]:
    """Return the values visible from the right side of the tree."""
    if root is None:
        return []
    result: list[int] = []
    queue: deque[TreeNode] = deque([root])
    while queue:
        last_val = 0
        for _ in range(len(queue)):
            node = queue.popleft()
            last_val = node.val
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        result.append(last_val)
    return result


if __name__ == "__main__":
    tree = TreeNode(
        1,
        TreeNode(2, None, TreeNode(5)),
        TreeNode(3, None, TreeNode(4)),
    )
    assert right_side_view(tree) == [1, 3, 4]
    assert right_side_view(TreeNode(1, None, TreeNode(3))) == [1, 3]
    assert right_side_view(None) == []
    assert right_side_view(TreeNode(1)) == [1]
    # Left spine only: every level's sole node is visible
    left_spine = TreeNode(1, TreeNode(2, TreeNode(3)))
    assert right_side_view(left_spine) == [1, 2, 3]
    print("binary_tree_right_side_view: OK")
