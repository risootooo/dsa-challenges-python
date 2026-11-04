"""
Problem: Cheapest Flights Within K Stops
There are n cities and flights[i] = (from, to, price). Return the cheapest
price from src to dst using at most k stops (k+1 flights), or -1 if no such
route exists.
Example: n=4, flights=[[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]],
         src=0, dst=3, k=1 -> 700

Approach: Bellman-Ford bounded by rounds. One relaxation round extends every
reachable route by exactly one flight, so after k+1 rounds the distance array
holds the best price using at most k stops. Each round relaxes from a copy of
the previous round's distances — relaxing in place would let a single round
chain several flights and silently break the stop limit.

Time Complexity: O(k * E)
Space Complexity: O(n)
"""

from __future__ import annotations

import math


def find_cheapest_price(
    n: int, flights: list[list[int]], src: int, dst: int, k: int
) -> int:
    """Return the cheapest src->dst price with at most k stops, else -1."""
    dist = [math.inf] * n
    dist[src] = 0
    for _ in range(k + 1):
        previous = dist[:]  # freeze: one round = one extra flight
        for u, v, price in flights:
            if previous[u] != math.inf and previous[u] + price < dist[v]:
                dist[v] = previous[u] + price
    return -1 if dist[dst] == math.inf else int(dist[dst])


if __name__ == "__main__":
    flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
    assert find_cheapest_price(4, flights, 0, 3, 1) == 700
    assert find_cheapest_price(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0) == 500
    assert find_cheapest_price(3, [[0, 1, 100]], 0, 2, 1) == -1
    print("cheapest_flights_within_k_stops: OK")
