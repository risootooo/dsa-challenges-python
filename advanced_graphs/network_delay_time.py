"""
Problem: Network Delay Time
A signal is sent from node k in a network of n nodes (labelled 1..n).
times[i] = (u, v, w) means it takes w time for the signal to travel the
directed edge u -> v. Return the time until all nodes receive the signal,
or -1 if some node is unreachable.
Example: times=[[2,1,1],[2,3,1],[3,4,1]], n=4, k=2 -> 2

Approach: Dijkstra from k. The answer is the maximum shortest-path distance
(the last node to hear the signal); if any distance stays infinite, the
signal never reaches everywhere and the answer is -1.

Time Complexity: O((V + E) log V)
Space Complexity: O(V + E)
"""

from __future__ import annotations

import heapq
import math


def network_delay_time(times: list[list[int]], n: int, k: int) -> int:
    """Return the time for a signal from `k` to reach all n nodes, else -1."""
    adjacency: list[list[tuple[int, int]]] = [[] for _ in range(n + 1)]
    for u, v, w in times:
        adjacency[u].append((v, w))

    dist = [math.inf] * (n + 1)
    dist[k] = 0
    heap: list[tuple[float, int]] = [(0, k)]
    while heap:
        d, node = heapq.heappop(heap)
        if d > dist[node]:
            continue
        for neighbour, weight in adjacency[node]:
            nd = d + weight
            if nd < dist[neighbour]:
                dist[neighbour] = nd
                heapq.heappush(heap, (nd, neighbour))

    answer = max(dist[1:])
    return -1 if answer == math.inf else int(answer)


if __name__ == "__main__":
    assert network_delay_time([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2) == 2
    assert network_delay_time([[1, 2, 1]], 2, 1) == 1
    assert network_delay_time([[1, 2, 1]], 2, 2) == -1
    print("network_delay_time: OK")
