"""
Problem: Merge Intervals
Given a collection of intervals [start, end], merge all overlapping
intervals and return the non-overlapping intervals that cover all of
the input, sorted by start.
Example: [[1,3],[2,6],[8,10],[15,18]] -> [[1,6],[8,10],[15,18]];
[[1,4],[4,5]] -> [[1,5]]

Approach: Sort the intervals by start, then sweep once keeping the
interval currently being built. Each next interval either overlaps
the current one (its start is at most the current end, so touching
endpoints count as overlapping) and extends it to the larger end, or
is disjoint and closes the current interval out. Sorting dominates
the running time. The input is not mutated: the sweep works on
sorted copies of the pairs.

Time Complexity: O(n log n)
Space Complexity: O(n)
"""

from __future__ import annotations


def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    """Return ``intervals`` with all overlaps merged, sorted by start."""
    if not intervals:
        return []
    ordered = sorted((list(pair) for pair in intervals), key=lambda p: p[0])
    merged: list[list[int]] = [ordered[0]]
    for start, end in ordered[1:]:
        last = merged[-1]
        if start <= last[1]:
            last[1] = max(last[1], end)
        else:
            merged.append([start, end])
    return merged


if __name__ == "__main__":
    assert merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]) == [
        [1, 6],
        [8, 10],
        [15, 18],
    ]
    assert merge_intervals([[1, 4], [4, 5]]) == [[1, 5]]
    # Unsorted input comes back sorted; a fully nested interval is absorbed
    assert merge_intervals([[8, 10], [1, 3], [2, 6]]) == [[1, 6], [8, 10]]
    assert merge_intervals([[1, 10], [2, 3], [4, 5]]) == [[1, 10]]
    assert merge_intervals([[1, 4]]) == [[1, 4]]
    assert merge_intervals([]) == []
    # Input must not be mutated
    data = [[2, 6], [1, 3]]
    merge_intervals(data)
    assert data == [[2, 6], [1, 3]]
    print("merge_intervals: OK")
