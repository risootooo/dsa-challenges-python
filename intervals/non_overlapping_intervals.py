"""
Problem: Non-overlapping Intervals
Given a collection of intervals [start, end], return the minimum number
of intervals to remove so that the remaining intervals are all
non-overlapping. Touching endpoints (for example [1, 2] and [2, 3]) do
not count as overlapping.
Example: [[1,2],[2,3],[3,4],[1,3]] -> 1 (remove [1,3]);
[[1,2],[1,2],[1,2]] -> 2; [[1,2],[2,3]] -> 0

Approach: Greedy by earliest end time. Sort the intervals by end (ties
broken by start), then keep an interval whenever it starts at or after
the end of the last kept interval; every other interval must be
removed. Keeping the interval that finishes soonest can never hurt: it
leaves at least as much room for everything that follows as any other
choice, so the greedy count of kept intervals is maximal and the
removals are minimal. Sorting dominates the running time. The input
is not mutated: the sweep works on sorted copies of the pairs.

Time Complexity: O(n log n)
Space Complexity: O(n)
"""

from __future__ import annotations


def erase_overlap_intervals(intervals: list[list[int]]) -> int:
    """Return the minimum removals so the rest do not overlap."""
    if not intervals:
        return 0
    ordered = sorted((list(pair) for pair in intervals), key=lambda p: (p[1], p[0]))
    removed = 0
    last_end = ordered[0][1]
    for start, end in ordered[1:]:
        if start < last_end:
            removed += 1
        else:
            last_end = end
    return removed


if __name__ == "__main__":
    assert erase_overlap_intervals([[1, 2], [2, 3], [3, 4], [1, 3]]) == 1
    assert erase_overlap_intervals([[1, 2], [1, 2], [1, 2]]) == 2
    assert erase_overlap_intervals([[1, 2], [2, 3]]) == 0
    # Unsorted input; a fully nested interval forces one removal
    assert erase_overlap_intervals([[3, 4], [1, 2], [2, 3]]) == 0
    assert erase_overlap_intervals([[1, 10], [2, 3], [4, 5]]) == 1
    assert erase_overlap_intervals([[1, 4]]) == 0
    assert erase_overlap_intervals([]) == 0
    # Input must not be mutated
    data = [[2, 3], [1, 2]]
    erase_overlap_intervals(data)
    assert data == [[2, 3], [1, 2]]
    print("non_overlapping_intervals: OK")
