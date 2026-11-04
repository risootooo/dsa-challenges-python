"""
Problem: Dijkstra's Shortest Path
Given a weighted graph with non-negative edge weights, n nodes labelled
0..n-1 and edges as (u, v, w) triples (undirected), compute the shortest
distance from a source node to every node. Unreachable nodes get -1.
Example: n=3, edges=[[0,1,1],[1,2,1],[0,2,4]], src=0 -> [0, 1, 2]

Approach: Dijkstra with a binary-heap priority queue. Repeatedly pop the
unsettled node with the smallest tentative distance — with non-negative
weights that distance is final — and relax its outgoing edges. Stale heap
entries (a node pushed with a larger distance than its recorded best) are
skipped. Requires non-negative weights; for negative edges use Bellman-Ford.

Time Complexity: O((V + E) log V)
Space Complexity: O(V + E)
"""

from __future__ import annotations

import heapq
import math


def shortest_paths(n: int, edges: list[list[int]], src: int) -> list[float]:
    """Return shortest distances from `src`; -1 for unreachable nodes."""
    adjacency: list[list[tuple[int, int]]] = [[] for _ in range(n)]
    for u, v, w in edges:
        adjacency[u].append((v, w))
        adjacency[v].append((u, w))

    dist = [math.inf] * n
    dist[src] = 0
    heap: list[tuple[float, int]] = [(0, src)]
    while heap:
        d, node = heapq.heappop(heap)
        if d > dist[node]:
            continue  # stale entry; a shorter path was already settled
        for neighbour, weight in adjacency[node]:
            nd = d + weight
            if nd < dist[neighbour]:
                dist[neighbour] = nd
                heapq.heappush(heap, (nd, neighbour))
    return [-1 if d == math.inf else d for d in dist]


if __name__ == "__main__":
    assert shortest_paths(3, [[0, 1, 1], [1, 2, 1], [0, 2, 4]], 0) == [0, 1, 2]
    assert shortest_paths(4, [[0, 1, 5]], 0) == [0, 5, -1, -1]
    print("dijkstra: OK")
