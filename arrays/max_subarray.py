"""
Problem: Maximum Subarray
Given an integer array, find the contiguous subarray with the largest sum
and return that sum.
Example: [-2, 1, -3, 4, -1, 2, 1, -5, 4] -> 6  (subarray [4, -1, 2, 1])

Approach: Kadane's algorithm. Scan once, keeping the best sum of a subarray
ending at the current position. If the running sum becomes negative, it can
only hurt any future subarray, so restart at the current element.

Time Complexity: O(n)
Space Complexity: O(1)
"""

from __future__ import annotations


def max_subarray(nums: list[int]) -> int:
    """Return the largest sum of any contiguous non-empty subarray."""
    if not nums:
        raise ValueError("nums must be non-empty")
    best = current = nums[0]
    for value in nums[1:]:
        current = max(value, current + value)
        best = max(best, current)
    return best


if __name__ == "__main__":
    assert max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert max_subarray([1]) == 1
    assert max_subarray([5, 4, -1, 7, 8]) == 23
    print("max_subarray: OK")
