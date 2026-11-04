"""
Problem: Search in Rotated Sorted Array
A sorted array was rotated at an unknown pivot. Find a target in it.
Example: [4,5,6,7,0,1,2], target=0 -> 4

Approach: In every step, at least one half of the current interval is
normally sorted. Check whether the target lies in the sorted half; if so
search there, otherwise search the other half.

Time Complexity: O(log n)
Space Complexity: O(1)
"""

from __future__ import annotations


def search_rotated(nums: list[int], target: int) -> int:
    """Return the index of ``target`` in a rotated sorted array, or -1."""
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[lo] <= nums[mid]:  # left half is sorted
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:  # right half is sorted
            if nums[mid] < target <= nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1


if __name__ == "__main__":
    assert search_rotated([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert search_rotated([4, 5, 6, 7, 0, 1, 2], 3) == -1
    print("search_in_rotated_sorted_array: OK")
