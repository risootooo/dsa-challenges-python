"""
Problem: Binary Search
Find the index of a target in a sorted array, or -1 if absent.
Example: [-1, 0, 3, 5, 9, 12], target=9 -> 4

Approach: Halve the search interval each step by comparing the target
with the middle element.

Time Complexity: O(log n)
Space Complexity: O(1)
"""

from __future__ import annotations


def binary_search(nums: list[int], target: int) -> int:
    """Return the index of ``target`` in sorted ``nums``, or -1."""
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


if __name__ == "__main__":
    assert binary_search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert binary_search([-1, 0, 3, 5, 9, 12], 2) == -1
    print("binary_search: OK")
