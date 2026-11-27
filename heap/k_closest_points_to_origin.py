"""
Problem: K Closest Points to Origin
Given points on a plane and an integer k, return the k points closest to
the origin (0, 0) by Euclidean distance. If two points are equally close,
either may be returned. The answer may be in any order.
Example: points = [[1, 3], [-2, 2]], k = 1 -> [[-2, 2]]
         points = [[3, 3], [5, -1], [-2, 4]], k = 2 -> [[3, 3], [-2, 4]]

Approach: Max-heap of size k keyed by negative squared distance. Squared
distance preserves the ordering and avoids a square root. Push each point
with its negated squared distance; whenever the heap grows past k, pop the
largest distance (the smallest negated key). What remains is exactly the
k closest points. A non-positive k, or no points, returns an empty list;
k larger than the number of points returns every point.

Time Complexity: O(n log k)
Space Complexity: O(k)
"""

from __future__ import annotations

import heapq


def k_closest(points: list[list[int]], k: int) -> list[list[int]]:
    """Return the ``k`` points in ``points`` closest to the origin."""
    if k <= 0 or not points:
        return []
    if k >= len(points):
        return [list(point) for point in points]
    # Entries are (-squared_distance, index, point); the index breaks ties
    # without ever comparing the point lists themselves.
    heap: list[tuple[int, int, list[int]]] = []
    for index, point in enumerate(points):
        dist_sq = point[0] * point[0] + point[1] * point[1]
        heapq.heappush(heap, (-dist_sq, index, list(point)))
        if len(heap) > k:
            heapq.heappop(heap)
    return [point for _, _, point in heap]


if __name__ == "__main__":
    def as_set(result: list[list[int]]) -> set[tuple[int, int]]:
        return {tuple(point) for point in result}

    assert as_set(k_closest([[1, 3], [-2, 2]], 1)) == {(-2, 2)}
    assert as_set(k_closest([[3, 3], [5, -1], [-2, 4]], 2)) == {(3, 3), (-2, 4)}
    assert as_set(k_closest([[0, 0], [1, 1], [2, 2]], 2)) == {(0, 0), (1, 1)}
    # Edge cases: empty input, single point, non-positive k, k beyond n
    assert k_closest([], 3) == []
    assert k_closest([[5, 5]], 1) == [[5, 5]]
    assert k_closest([[1, 1], [2, 2]], 0) == []
    assert as_set(k_closest([[2, 2], [1, 1]], 5)) == {(1, 1), (2, 2)}
    print("k_closest_points_to_origin: OK")
