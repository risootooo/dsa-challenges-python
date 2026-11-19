"""
Problem: Find Minimum in Rotated Sorted Array
A strictly increasing list of distinct integers was rotated at an
unknown pivot (some prefix moved to the end, possibly the whole list,
i.e. no rotation). Return its minimum element in O(log n) time.
Example: nums=[3,4,5,1,2] -> 1; nums=[4,5,6,7,0,1,2] -> 0;
nums=[11,13,15,17] -> 11

Approach: Binary search against the right endpoint. If nums[mid] is
greater than nums[hi], the rotation point — and so the minimum — lies
strictly to the right of mid, so discard the left half including mid.
Otherwise nums[mid] is at most nums[hi], the minimum is at mid or to
its left, and mid itself stays a candidate, so set hi = mid rather
than mid - 1. The interval shrinks every step and lo == hi lands on
the minimum. An empty list has no minimum, so the function returns
None; a single-element list returns that element.

Time Complexity: O(log n)
Space Complexity: O(1)
"""

from __future__ import annotations


def find_min(nums: list[int]) -> int | None:
    """Return the minimum of a rotated strictly-increasing list.

    Returns None for an empty list. The input is not mutated.
    """
    if not nums:
        return None
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] > nums[hi]:
            lo = mid + 1
        else:
            hi = mid
    return nums[lo]


if __name__ == "__main__":
    assert find_min([3, 4, 5, 1, 2]) == 1
    assert find_min([4, 5, 6, 7, 0, 1, 2]) == 0
    assert find_min([11, 13, 15, 17]) == 11
    # Edge cases: empty input, single element, two elements, no rotation
    assert find_min([]) is None
    assert find_min([1]) == 1
    assert find_min([2, 1]) == 1
    assert find_min([1, 2]) == 1
    assert find_min([2, 3, 4, 5, 1]) == 1
    assert find_min([-5, -2, 0, -10, -7]) == -10
    print("find_minimum_in_rotated_sorted_array: OK")
