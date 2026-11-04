"""
Problem: Product of Array Except Self
Given an array nums, return an array where each element is the product of
all elements of nums except the element at that index. Do not use division.
Example: [1, 2, 3, 4] -> [24, 12, 8, 6]

Approach: Two passes. First pass stores the product of everything to the
left of each index; second pass multiplies by a running product of
everything to the right.

Time Complexity: O(n)
Space Complexity: O(1) extra (excluding the output array)
"""

from __future__ import annotations


def product_except_self(nums: list[int]) -> list[int]:
    """Return products of all other elements, without using division."""
    n = len(nums)
    result = [1] * n
    left = 1
    for i in range(n):
        result[i] = left
        left *= nums[i]
    right = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right
        right *= nums[i]
    return result


if __name__ == "__main__":
    assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert product_except_self([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
    print("product_except_self: OK")
