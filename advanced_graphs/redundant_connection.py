"""
Problem: Redundant Connection
A graph that started as a tree of n nodes (labelled 1..n) had one extra edge
added. Return the edge that can be removed so the graph becomes a tree —
specifically the last such edge in the input order.
Example: edges=[[1,2],[1,3],[2,3]] -> [2,3]
         edges=[[1,2],[2,3],[3,4],[1,4],[1,5]] -> [1,4]

Approach: Union-Find (disjoint set union) with path compression and union by
rank. Process edges in order: each edge joins two components, unless its
endpoints are already connected — that edge closes a cycle and is exactly
the redundant one.

Time Complexity: O(n * alpha(n)), alpha = inverse Ackermann (near-constant)
Space Complexity: O(n)
"""

from __future__ import annotations


class UnionFind:
    """Disjoint set union with path compression and union by rank."""

    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x: int) -> int:
        while self.parent[x] != x:  # path halving
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x: int, y: int) -> bool:
        """Join the sets of x and y. Return False if already joined."""
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        return True


def find_redundant_connection(edges: list[list[int]]) -> list[int]:
    """Return the edge whose removal turns the graph back into a tree."""
    uf = UnionFind(len(edges) + 1)
    for u, v in edges:
        if not uf.union(u, v):
            return [u, v]
    return []


if __name__ == "__main__":
    assert find_redundant_connection([[1, 2], [1, 3], [2, 3]]) == [2, 3]
    assert find_redundant_connection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]) == [1, 4]
    print("redundant_connection: OK")
