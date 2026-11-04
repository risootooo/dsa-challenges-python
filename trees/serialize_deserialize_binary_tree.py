"""
Problem: Serialize and Deserialize Binary Tree
Design an encoding of a binary tree to a string and its exact inverse, so
that deserialize(serialize(root)) reconstructs an identical tree.
Example: tree [1,2,3,null,null,4,5] serializes to "1,2,3,null,null,4,5,..."
         (level-order with explicit nulls); decoding restores the same tree.

Approach: Level-order (BFS) encoding: emit node values in breadth-first
order, writing "null" for missing children, joined by commas. Decoding
replays the same order with a queue — each dequeued node consumes the next
two tokens as its left and right children. BFS is chosen over preorder
because the format is human-inspectable and streaming-friendly; both are
O(n). Trailing null tokens are trimmed on encode and tolerated on decode.

Time Complexity: O(n) for serialize and deserialize
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


class Codec:
    """Level-order serializer/deserializer for binary trees."""

    def serialize(self, root: TreeNode | None) -> str:
        if root is None:
            return ""
        tokens: list[str] = []
        queue: deque[TreeNode | None] = deque([root])
        while queue:
            node = queue.popleft()
            if node is None:
                tokens.append("null")
            else:
                tokens.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
        while tokens and tokens[-1] == "null":
            tokens.pop()
        return ",".join(tokens)

    def deserialize(self, data: str) -> TreeNode | None:
        if not data:
            return None
        tokens = data.split(",")
        root = TreeNode(int(tokens[0]))
        queue: deque[TreeNode] = deque([root])
        i = 1
        while queue and i < len(tokens):
            node = queue.popleft()
            if tokens[i] != "null":
                node.left = TreeNode(int(tokens[i]))
                queue.append(node.left)
            i += 1
            if i < len(tokens) and tokens[i] != "null":
                node.right = TreeNode(int(tokens[i]))
                queue.append(node.right)
            i += 1
        return root


if __name__ == "__main__":
    codec = Codec()
    tree = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
    encoded = codec.serialize(tree)
    assert encoded == "1,2,3,null,null,4,5"
    decoded = codec.deserialize(encoded)
    assert codec.serialize(decoded) == encoded
    assert codec.serialize(None) == ""
    assert codec.deserialize("") is None
    print("serialize_deserialize_binary_tree: OK")
