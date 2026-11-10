"""
Problem: Insert Interval
Given a list of non-overlapping intervals sorted by start, and a new
interval, insert the new interval and merge if necessary so the
result is still sorted and non-overlapping.
Example: [[1,3],[6,9]] with [2,5] -> [[1,5],[6,9]];
[[1,2],[3,5],[6,7],[8,10],[12,16]] with [4,8] -> [[1,2],[3,10],[12,16]]

Approach: One linear sweep in three phases, exploiting that the
input is already sorted and disjoint. First copy every interval that
ends before the new interval starts. Then merge every interval that
overlaps or touches the new one by widening the new interval to the
min start / max end. Finally copy the remaining intervals, which all
start after the merged interval ends. Touching endpoints count as
overlapping, matching Merge Intervals. Neither the input list nor
the new interval is mutated.

Time Complexity: O(n)
Space Complexity: O(n) for the output
"""

from __future__ import annotations


def insert_interval(
    intervals: list[list[int]], new_interval: list[int]
) -> list[list[int]]:
    """Insert ``new_interval`` into sorted disjoint ``intervals``, merging overlaps."""
    result: list[list[int]] = []
    start, end = new_interval[0], new_interval[1]
    i, n = 0, len(intervals)

    # Phase 1: intervals entirely before the new one.
    while i < n and intervals[i][1] < start:
        result.append(list(intervals[i]))
        i += 1

    # Phase 2: merge every interval overlapping or touching the new one.
    while i < n and intervals[i][0] <= end:
        start = min(start, intervals[i][0])
        end = max(end, intervals[i][1])
        i += 1
    result.append([start, end])

    # Phase 3: intervals entirely after the merged one.
    while i < n:
        result.append(list(intervals[i]))
        i += 1

    return result


if __name__ == "__main__":
    assert insert_interval([[1, 3], [6, 9]], [2, 5]) == [[1, 5], [6, 9]]
    assert insert_interval(
        [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]
    ) == [[1, 2], [3, 10], [12, 16]]
    # Disjoint inserts at the head, middle and tail keep the sort order
    assert insert_interval([[3, 4], [6, 7]], [1, 2]) == [[1, 2], [3, 4], [6, 7]]
    assert insert_interval([[1, 2], [6, 7]], [3, 4]) == [[1, 2], [3, 4], [6, 7]]
    assert insert_interval([[1, 2], [3, 4]], [6, 7]) == [[1, 2], [3, 4], [6, 7]]
    # Touching endpoints merge; a covering interval absorbs everything
    assert insert_interval([[1, 3], [5, 7]], [3, 5]) == [[1, 7]]
    assert insert_interval([[2, 3], [5, 6]], [1, 10]) == [[1, 10]]
    # Edge cases: empty list, single interval
    assert insert_interval([], [5, 7]) == [[5, 7]]
    assert insert_interval([[1, 2]], [3, 4]) == [[1, 2], [3, 4]]
    # Inputs must not be mutated
    data, new = [[1, 3], [6, 9]], [2, 5]
    insert_interval(data, new)
    assert data == [[1, 3], [6, 9]] and new == [2, 5]
    print("insert_interval: OK")
