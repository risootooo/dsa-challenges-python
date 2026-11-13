"""
Problem: Meeting Rooms
Given a list of meeting time intervals [start, end], determine whether
a single person could attend every meeting — that is, whether no two
meetings overlap. Meetings that touch at an endpoint (one ends exactly
when the next starts) do not overlap.
Example: [[0,30],[5,10],[15,20]] -> False;
[[7,10],[2,4]] -> True

Approach: Sort the intervals by start, then check each adjacent pair
in that order. If any meeting starts before the previous one ends,
the two overlap and attendance is impossible. Adjacent checks are
enough: after sorting, any overlap must show up between neighbours,
because a meeting that cleared its immediate predecessor starts at
or after every earlier meeting's start and, by the chain of
non-overlaps, at or after their ends too. Touching endpoints pass,
since the check is a strict less-than. The input is not mutated: the
sort works on copies of the pairs.

Time Complexity: O(n log n)
Space Complexity: O(n) for the sorted copy
"""

from __future__ import annotations


def can_attend_meetings(intervals: list[list[int]]) -> bool:
    """Return True iff no two meetings in ``intervals`` overlap."""
    if len(intervals) <= 1:
        return True
    ordered = sorted((list(pair) for pair in intervals), key=lambda p: p[0])
    for i in range(1, len(ordered)):
        if ordered[i][0] < ordered[i - 1][1]:
            return False
    return True


if __name__ == "__main__":
    assert can_attend_meetings([[0, 30], [5, 10], [15, 20]]) is False
    assert can_attend_meetings([[7, 10], [2, 4]]) is True
    # Touching endpoints do not overlap
    assert can_attend_meetings([[0, 5], [5, 10], [10, 15]]) is True
    # Unsorted input; a fully nested meeting still overlaps
    assert can_attend_meetings([[15, 20], [0, 30]]) is False
    assert can_attend_meetings([[1, 10], [2, 3]]) is False
    # Edge cases: empty input, single meeting
    assert can_attend_meetings([]) is True
    assert can_attend_meetings([[1, 4]]) is True
    # Input must not be mutated
    data = [[7, 10], [2, 4]]
    can_attend_meetings(data)
    assert data == [[7, 10], [2, 4]]
    print("meeting_rooms: OK")
