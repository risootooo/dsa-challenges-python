"""
Problem: Longest Consecutive Sequence
Given an unsorted list of integers, return the length of the longest
sequence of consecutive integers that can be formed from its values.
The values themselves need not appear consecutively in the input.
Example: nums=[100,4,200,1,3,2] -> 4 (1,2,3,4); nums=[0,3,7,2,5,8,4,6,0,1]
-> 9 (0,1,2,3,4,5,6,7,8); nums=[] -> 0

Approach: Hash set with sequence-start detection. Put every value in a
set for O(1) membership. A value x can only start a run when x - 1 is
absent from the set, so each run is walked exactly once, from its true
start, counting x, x + 1, x + 2, ... while successors are present.
Values that are not starts are skipped in O(1), so the total work is
linear even though runs are scanned element by element. Duplicate
values collapse in the set and cannot extend a run twice.

Time Complexity: O(n)
Space Complexity: O(n)
"""

from __future__ import annotations


def longest_consecutive(nums: list[int]) -> int:
    """Return the length of the longest consecutive-values run in ``nums``.

    Returns 0 for an empty list. The input is not mutated.
    """
    values = set(nums)
    best = 0
    for x in values:
        if x - 1 in values:
            continue
        length = 1
        while x + length in values:
            length += 1
        if length > best:
            best = length
    return best


if __name__ == "__main__":
    assert longest_consecutive([100, 4, 200, 1, 3, 2]) == 4
    assert longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
    assert longest_consecutive([1, 0, 1, 2]) == 3
    # Edge cases: empty input, single element, duplicates, negatives
    assert longest_consecutive([]) == 0
    assert longest_consecutive([7]) == 1
    assert longest_consecutive([5, 5, 5]) == 1
    assert longest_consecutive([-3, -2, -1, 1, 2]) == 3
    assert longest_consecutive([9, 8, 7, 6, 5]) == 5
    print("longest_consecutive_sequence: OK")
