"""
Problem: Find Peak Element
A peak element is strictly greater than its neighbours; elements
outside the list count as negative infinity, and adjacent elements
are never equal. Return the index of any one peak.
Example: nums=[1,2,3,1] -> 2; nums=[1,2,1,3,5,6,4] -> 5 (or 1)

Approach: Binary search on the slope. If nums[mid] is smaller than
nums[mid + 1], the list is rising at mid, so a peak must lie strictly
to the right (keep climbing). Otherwise the list is falling at mid,
so mid itself or something to its left is a peak, and mid stays a
candidate (hi = mid, not mid - 1). The interval shrinks every step
and lo == hi lands on a peak: the search can never walk off an edge,
because the out-of-range side counts as negative infinity. An empty
list has no peak, so the function returns None.

Time Complexity: O(log n)
Space Complexity: O(1)
"""

from __future__ import annotations


def find_peak_element(nums: list[int]) -> int | None:
    """Return the index of a peak element, or None for an empty list.

    The input is not mutated.
    """
    if not nums:
        return None
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] < nums[mid + 1]:
            lo = mid + 1
        else:
            hi = mid
    return lo


if __name__ == "__main__":
    assert find_peak_element([1, 2, 3, 1]) == 2
    assert find_peak_element([1, 2, 1, 3, 5, 6, 4]) == 5
    # Monotone lists peak at an endpoint
    assert find_peak_element([1, 2, 3, 4]) == 3
    assert find_peak_element([4, 3, 2, 1]) == 0
    # A valley's neighbours are both peaks; either answer is valid,
    # and this search returns the right-hand one
    assert find_peak_element([3, 1, 2]) == 2
    assert find_peak_element([2, 1]) == 0
    assert find_peak_element([1, 2]) == 1
    # Edge cases: empty input, single element
    assert find_peak_element([]) is None
    assert find_peak_element([42]) == 0
    print("find_peak_element: OK")
