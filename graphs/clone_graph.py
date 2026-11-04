"""
Problem: Clone Graph
Given a reference to a node in a connected undirected graph, return a deep
copy of the graph. Each node has a value and a list of neighbours.
Example: adjacency [[2,4],[1,3],[2,4],[1,3]] -> an isomorphic copy whose
         nodes are all new objects.

Approach: Iterative DFS with an explicit stack and a {original: clone} map.
The map is the whole trick: create the clone the first time a node is seen,
so cycles terminate and every edge is wired exactly once between clones.
A BFS with a queue works identically; DFS keeps the code shorter.

Time Complexity: O(V + E)
Space Complexity: O(V)
"""

from __future__ import annotations


class Node:
    """Undirected graph node, as used by the classic problem statement."""

    def __init__(self, val: int = 0, neighbors: list["Node"] | None = None):
        self.val = val
        self.neighbors = list(neighbors) if neighbors else []

    def __repr__(self) -> str:  # pragma: no cover - debugging aid
        return f"Node({self.val})"


def clone_graph(node: Node | None) -> Node | None:
    """Return a deep copy of the graph reachable from ``node``."""
    if node is None:
        return None
    clones: dict[Node, Node] = {node: Node(node.val)}
    stack = [node]
    while stack:
        original = stack.pop()
        for neighbor in original.neighbors:
            if neighbor not in clones:
                clones[neighbor] = Node(neighbor.val)
                stack.append(neighbor)
            clones[original].neighbors.append(clones[neighbor])
    return clones[node]


if __name__ == "__main__":
    # Build the 4-node cycle 1-2-3-4-1 and verify structure + independence.
    n1, n2, n3, n4 = Node(1), Node(2), Node(3), Node(4)
    n1.neighbors, n2.neighbors = [n2, n4], [n1, n3]
    n3.neighbors, n4.neighbors = [n2, n4], [n1, n3]
    copy_root = clone_graph(n1)
    assert copy_root is not n1 and copy_root.val == 1
    assert sorted(n.val for n in copy_root.neighbors) == [2, 4]
    copy_root.neighbors[0].val = 99  # mutating the copy...
    assert n2.val == 2  # ...must not touch the original
    print("clone_graph: OK")
