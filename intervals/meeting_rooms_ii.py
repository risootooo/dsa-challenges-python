"""
Problem: Meeting Rooms II
Given a list of meeting time intervals [start, end], return the
minimum number of rooms required so that every meeting can take
place. Meetings that touch at an endpoint (one ends exactly when
the next starts) can share a room.
Example: [[0,30],[5,10],[15,20]] -> 2;
[[7,10],[2,4]] -> 1

Approach: Sweep the meetings in start order with a min-heap of the
end times of the meetings currently occupying a room. For each new
meeting, if the room that frees up earliest is free by the time it
starts (earliest end <= start), reuse that room by replacing its end
time; otherwise every room is busy at its start and a new room is
needed. The heap size at the end is the peak number of simultaneous
meetings, which is exactly the number of rooms required: no schedule
can use fewer (those meetings all overlap at one instant), and this
greedy reuse shows that many always suffice. The input is not
mutated: the sweep works on copies of the pairs.

Time Complexity: O(n log n)
Space Complexity: O(n) for the heap and the sorted copy
"""

from __future__ import annotations

import heapq


def min_meeting_rooms(intervals: list[list[int]]) -> int:
    """Return the minimum number of rooms needed for ``intervals``."""
    if not intervals:
        return 0
    ordered = sorted((list(pair) for pair in intervals), key=lambda p: (p[0], p[1]))
    ends: list[int] = []  # min-heap of end times of rooms in use
    for start, end in ordered:
        if ends and ends[0] <= start:
            heapq.heapreplace(ends, end)
        else:
            heapq.heappush(ends, end)
    return len(ends)


if __name__ == "__main__":
    assert min_meeting_rooms([[0, 30], [5, 10], [15, 20]]) == 2
    assert min_meeting_rooms([[7, 10], [2, 4]]) == 1
    # Touching endpoints can share a room
    assert min_meeting_rooms([[0, 5], [5, 10], [10, 15]]) == 1
    # Fully nested meetings each need their own room
    assert min_meeting_rooms([[1, 10], [2, 9], [3, 8]]) == 3
    # Unsorted input; two disjoint chains interleaved
    assert min_meeting_rooms([[15, 20], [0, 10], [5, 12], [11, 16]]) == 2
    assert min_meeting_rooms([[1, 5], [1, 5], [1, 5]]) == 3
    # Edge cases: empty input, single meeting
    assert min_meeting_rooms([]) == 0
    assert min_meeting_rooms([[1, 4]]) == 1
    # Input must not be mutated
    data = [[7, 10], [2, 4]]
    min_meeting_rooms(data)
    assert data == [[7, 10], [2, 4]]
    print("meeting_rooms_ii: OK")
